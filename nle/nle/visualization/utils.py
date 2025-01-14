import cv2
import os
import numpy as np
from collections import namedtuple, Counter, defaultdict
import re
import copy
from PIL import Image, ImageDraw, ImageFont

from nle import nethack

script_dir = os.path.dirname(__file__)

image_rel_path = "3.6.1tiles32.png"
image_abs_path = os.path.join(script_dir, image_rel_path)

tileset = cv2.imread(image_abs_path)[..., ::-1]

tile_size = 32
h = tileset.shape[0] // tile_size
w = tileset.shape[1] // tile_size
tiles = []
for y in range(h):
    y *= tile_size
    for x in range(w):
        x *= tile_size
        tiles.append(tileset[y:y + tile_size, x:x + tile_size])

tileset = np.array(tiles)

glyph2tile = np.array(nethack.glyph2tile)

BLStats = namedtuple('BLStats',
                     'x y strength_percentage strength dexterity constitution intelligence wisdom charisma score hitpoints max_hitpoints depth gold energy max_energy armor_class monster_level experience_level experience_points time hunger_state carrying_capacity dungeon_number level_number prop_mask')

FONT_SIZE = 32
HISTORY_SIZE = 13


def draw_grid(imgs, ncol):
    grid = imgs.reshape((-1, ncol, *imgs[0].shape))
    rows = []
    for row in grid:
        rows.append(np.concatenate(row, axis=1))

    return np.concatenate(rows, axis=0)


def draw_frame(img, color=(90, 90, 90), thickness=3):
    return cv2.rectangle(img, (0, 0), (img.shape[1] - 1, img.shape[0] - 1), color, thickness)


def draw_all(glyphs, agent, last_obs, steps, action_history, message_history, popup_history):
    tiles_idx = glyph2tile[glyphs]
    tiles = tileset[tiles_idx.reshape(-1)]

    scene_vis = draw_grid(tiles, glyphs.shape[1])
    glyph_frame = draw_frame(scene_vis)
    glyph_frame = cv2.cvtColor(glyph_frame, cv2.COLOR_BGR2RGB)

    height = FONT_SIZE * len(last_obs['tty_chars'])
    width = scene_vis.shape[1]

    try:
        stats_frame = draw_stats(agent, height, int(width / 2), steps)
    except:
        stats_frame = np.zeros((height, int(width / 2), 3), dtype=np.uint8)

    try:
        tty_frame = draw_tty(last_obs, height, int(width / 2))
    except:
        tty_frame = np.zeros((height, int(width / 2), 3), dtype=np.uint8)

    bottom_frame = np.concatenate([tty_frame, stats_frame], axis=1)
    frame = np.concatenate([glyph_frame, bottom_frame], axis=0)

    inventory_frame = draw_inventory(agent, last_obs, frame.shape[0], int(width / 3))

    action_history_frame = draw_action_history(action_history, int(width / 3))
    message_history_frame = draw_message_history(message_history, int(width / 2))
    popup_history_frame = draw_popup_history(popup_history, int(width / 2))

    frame = np.concatenate([frame, inventory_frame], axis=1)
    topbar_frame = np.concatenate([action_history_frame, message_history_frame, popup_history_frame], axis=1)

    frame = np.concatenate([topbar_frame, frame], axis=0)

    cv2.imshow("frame", frame)
    cv2.waitKey(1)


def draw_tty(last_obs, height, width):
    vis = np.zeros((int(height), int(width), 3)).astype(np.uint8)

    vis = Image.fromarray(vis)
    draw = ImageDraw.Draw(vis)

    font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf", int(26))

    for i, line in enumerate(last_obs['tty_chars']):
        txt = ''.join([chr(i) for i in line])
        draw.text((int(5), int((5 + i * 31))), txt, (255, 255, 255), font=font)

    vis = np.array(vis.resize((width, height), Image.ANTIALIAS))
    draw_frame(vis)

    return vis


def draw_action_history(action_history, width):
    vis = np.zeros((FONT_SIZE * HISTORY_SIZE, width, 3)).astype(np.uint8)
    for i in range(HISTORY_SIZE):
        if i >= len(action_history):
            break

        txt = action_history[-i - 1]
        if i == 0:
            put_text(vis, txt, (0, i * FONT_SIZE), color=(255, 255, 255))
        else:
            put_text(vis, txt, (0, i * FONT_SIZE), color=(120, 120, 120))

    draw_frame(vis)

    return vis


def draw_message_history(message_history, width):
    vis = np.zeros((FONT_SIZE * HISTORY_SIZE, width, 3)).astype(np.uint8)
    for i in range(HISTORY_SIZE):
        if i >= len(message_history):
            break

        txt = message_history[-i - 1]
        if i == 0:
            put_text(vis, txt, (0, i * FONT_SIZE), color=(255, 255, 255))
        else:
            put_text(vis, txt, (0, i * FONT_SIZE), color=(120, 120, 120))

    draw_frame(vis)

    return vis


def draw_popup_history(popup_history, width):
    vis = np.zeros((FONT_SIZE * HISTORY_SIZE, width, 3)).astype(np.uint8)
    for i in range(HISTORY_SIZE):
        if i >= len(popup_history):
            break

        txt = '|'.join(popup_history[-i - 1])
        if i == 0:
            put_text(vis, txt, (0, i * FONT_SIZE), color=(255, 255, 255))
        else:
            put_text(vis, txt, (0, i * FONT_SIZE), color=(120, 120, 120))

    draw_frame(vis)

    return vis


def parse_attribute(text):
    matches = re.findall('You are a ([a-z]+) (([a-z]+) )?([a-z]+) ([A-Z][a-z]+).', text)
    if len(matches) == 1:
        alignment, _, gender, race, role = matches[0]
    else:
        matches = re.findall(
            'You are an? ([a-zA-Z ]+), a level (\d+) (([a-z]+) )?([a-z]+) ([A-Z][a-z]+). *You are ([a-z]+)',
            text)
        #assert len(matches) == 1, repr(text)
        _, _, _, gender, race, role, alignment = matches[0]

    if not gender:
        if role == 'Priestess':
            gender = 'female'
        elif role == 'Priest':
            gender = 'male'
        elif role == 'Caveman':
            gender = 'male'
        elif role == 'Cavewoman':
            gender = 'female'
        elif role == 'Valkyrie':
            gender = 'female'
        else:
            assert 0, repr(text)

    return gender, race, role, alignment


def find_marker(lines, regex=re.compile(r"(--More--|\(end\)|\(\d+ of \d+\))")):
    """ Return (line, column) of markers:
    --More-- | (end) | (X of N)
    """
    if len(regex.findall(' '.join(lines))) > 1:
        raise ValueError('Too many markers')

    result, marker_type = None, None
    for i, line in enumerate(lines):
        res = regex.findall(line)
        if res:
            assert len(res) == 1
            j = line.find(res[0])
            result, marker_type = (i, j), res[0]
            break

    if result is not None and result[1] == 1:
        result = (result[0], 0)  # e.g. for known items view

    return result, marker_type


def get_message_and_popup(obs):
    """ Uses MORE action to get full popup and/or message.
    """
    message = bytes(obs['message']).decode().replace('\0', ' ').replace('\n', '').strip()
    if message.endswith('--More--'):
        # FIXME: It seems like in this case the environment doesn't expect additional input,
        #        but I'm not 100% sure, so it's too risky to change it, because it could stall everything.
        #        With the current implementation, in the worst case, we'll get "Unknown command ' '".
        message = message[:-len('--More--')]

    # assert '\n' not in message and '\r' not in message
    popup = []

    lines = [bytes(line).decode().replace('\0', ' ').replace('\n', '') for line in obs['tty_chars']]
    marker_pos, marker_type = find_marker(lines)

    if marker_pos is None:
        return message, popup, True

    pref = ''
    message_lines_count = 0
    if message:
        for i, line in enumerate(lines[:marker_pos[0] + 1]):
            if i == marker_pos[0]:
                line = line[:marker_pos[1]]
            message_lines_count += 1
            pref += line.strip()

            # I'm not sure when the new line character in broken messages should be a space and when be ignored.
            # '#' character (and others) occasionally occurs at the beginning of the broken line and isn't in
            # the message. Sometimes the message on the screen lacks last '.'.
            replace_func = lambda x: ''.join((c for c in x if c.isalnum()))
            if replace_func(pref) == replace_func(message):
                break
        else:
            if marker_pos[0] == 0:
                elems1 = [s for s in message.split() if s]
                elems2 = [s for s in pref.split() if s]
                assert len(elems1) < len(elems2) and elems2[-len(elems1):] == elems1, (elems1, elems2)
                return pref, popup, False

            raise ValueError(f"Message:\n{repr(message)}\ndoesn't match the screen:\n{repr(pref)}")

    # cut out popup
    for l in lines[message_lines_count:marker_pos[0]] + [lines[marker_pos[0]][:marker_pos[1]]]:
        l = l[marker_pos[1]:].strip()
        if l:
            popup.append(l)

    return message, popup, False


def put_text(img, text, pos, scale=FONT_SIZE / 35, thickness=1, color=(255, 255, 0), console=False):
    # TODO: figure out how exactly opencv anchors the text
    pos = (pos[0] + FONT_SIZE // 2, pos[1] + FONT_SIZE // 2 + 8)

    if console:
        # TODO: implement equal characters size font
        # scale *= 2
        # font = cv2.FONT_HERSHEY_PLAIN
        font = cv2.FONT_HERSHEY_SIMPLEX
    else:
        font = cv2.FONT_HERSHEY_SIMPLEX

    return cv2.putText(img, text, pos, font,
                       scale, color, thickness, cv2.LINE_AA)


UNKNOWN = -1  # for everything, e.g. alignment

ARCHEOLOGIST = 0
BARBARIAN = 1
CAVEMAN = 2
HEALER = 3
KNIGHT = 4
MONK = 5
PRIEST = 6
RANGER = 7
ROGUE = 8
SAMURAI = 9
TOURIST = 10
VALKYRIE = 11
WIZARD = 12

name_to_role = {
    'Archeologist': ARCHEOLOGIST,
    'Barbarian': BARBARIAN,
    'Caveman': CAVEMAN,
    'Cavewoman': CAVEMAN,
    'Healer': HEALER,
    'Knight': KNIGHT,
    'Monk': MONK,
    'Priest': PRIEST,
    'Priestess': PRIEST,
    'Ranger': RANGER,
    'Rogue': ROGUE,
    'Samurai': SAMURAI,
    'Tourist': TOURIST,
    'Valkyrie': VALKYRIE,
    'Wizard': WIZARD,
}

CHAOTIC = 0
NEUTRAL = 1
LAWFUL = 2
UNALIGNED = 3

name_to_alignment = {
    'chaotic': CHAOTIC,
    'neutral': NEUTRAL,
    'lawful': LAWFUL,
    'unaligned': UNALIGNED,
}

HUMAN = 0
DWARF = 1
ELF = 2
GNOME = 3
ORC = 4

name_to_race = {
    'human': HUMAN,
    'dwarf': DWARF,
    'dwarven': DWARF,
    'elf': ELF,
    'elven': ELF,
    'gnome': GNOME,
    'gnomish': GNOME,
    'orc': ORC,
    'orcish': ORC,
}

MALE = 0
FEMALE = 1

name_to_gender = {
    'male': MALE,
    'female': FEMALE,
}

possible_skill_types = ['Fighting Skills', 'Weapon Skills', 'Spellcasting Skills']
possible_skill_levels = ['Unskilled', 'Basic', 'Skilled', 'Expert', 'Master', 'Grand Master']

SKILL_LEVEL_RESTRICTED = 0
SKILL_LEVEL_UNSKILLED = 1
SKILL_LEVEL_BASIC = 2
SKILL_LEVEL_SKILLED = 3
SKILL_LEVEL_EXPERT = 4
SKILL_LEVEL_MASTER = 5
SKILL_LEVEL_GRAND_MASTER = 6

weapon_bonus = {
    SKILL_LEVEL_RESTRICTED: (-4, 2),
    SKILL_LEVEL_UNSKILLED: (-4, 2),
    SKILL_LEVEL_BASIC: (0, 0),
    SKILL_LEVEL_SKILLED: (2, 1),
    SKILL_LEVEL_EXPERT: (3, 2),
}
two_weapon_bonus = {
    SKILL_LEVEL_RESTRICTED: (-9, -3),
    SKILL_LEVEL_UNSKILLED: (-9, -3),
    SKILL_LEVEL_BASIC: (-7, -1),
    SKILL_LEVEL_SKILLED: (-5, 0),
    SKILL_LEVEL_EXPERT: (-3, 1),
}
riding_bonus = {
    SKILL_LEVEL_RESTRICTED: (-2, 0),
    SKILL_LEVEL_UNSKILLED: (-2, 0),
    SKILL_LEVEL_BASIC: (-1, 0),
    SKILL_LEVEL_SKILLED: (0, 1),
    SKILL_LEVEL_EXPERT: (0, 2),
}
unarmed_bonus = {
    SKILL_LEVEL_RESTRICTED: (1, 0),
    SKILL_LEVEL_UNSKILLED: (1, 0),
    SKILL_LEVEL_BASIC: (1, 1),
    SKILL_LEVEL_SKILLED: (2, 1),
    SKILL_LEVEL_EXPERT: (2, 2),
    SKILL_LEVEL_MASTER: (3, 2),
    SKILL_LEVEL_GRAND_MASTER: (3, 3),
}
martial_bonus = {
    SKILL_LEVEL_RESTRICTED: (1, 0),  # no one has it restricted
    SKILL_LEVEL_UNSKILLED: (2, 1),
    SKILL_LEVEL_BASIC: (3, 3),
    SKILL_LEVEL_SKILLED: (4, 4),
    SKILL_LEVEL_EXPERT: (5, 6),
    SKILL_LEVEL_MASTER: (6, 7),
    SKILL_LEVEL_GRAND_MASTER: (7, 9),
}

name_to_skill_level = {k: v for k, v in zip(['Restricted'] + possible_skill_levels,
                                            [SKILL_LEVEL_RESTRICTED,
                                             SKILL_LEVEL_UNSKILLED, SKILL_LEVEL_BASIC, SKILL_LEVEL_SKILLED,
                                             SKILL_LEVEL_EXPERT,
                                             SKILL_LEVEL_MASTER, SKILL_LEVEL_GRAND_MASTER])}
    


class Agent:
    def __init__(self):
        # x y strength_percentage strength dexterity constitution intelligence wisdom charisma score hitpoints max_hitpoints 
        # depth gold energy max_energy armor_class monster_level experience_level experience_points time hunger_state carrying_capacity 
        # dungeon_number level_number
        self.blstats = None
        self.gender = None
        self.race = None
        self.role = None
        self.alignment = None
        self.items = {}

    def update_blstats(self, blstats):
        self.blstats = blstats

    def update_chracters(self, role, alignment, race, gender):
        self.role = name_to_role[role]
        self.alignment = name_to_alignment[alignment]
        self.race = name_to_race[race]
        self.gender = name_to_gender[gender]

    def update_items(self, item_letters, item_glyphs, item_strs, item_oclasses):
        item_names = []
        for i, strs in enumerate(item_strs):
            name = bytes(strs).decode().strip('\0')
            if name != "":
                item_names.append(name)
                if name not in self.items:
                    letter = chr(item_letters[i])

                    tile_idx = glyph2tile[item_glyphs[i]]
                    image = tileset[tile_idx]
                    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
                    image = cv2.resize(image, dsize=(64, 64), interpolation=cv2.INTER_AREA)

                    cv2.putText(image, letter, (45, 25), cv2.FONT_HERSHEY_SIMPLEX, 
                                1, (255, 255, 255), 2, cv2.LINE_AA)

                    category = item_oclasses[i]

                    self.items[name] = [letter, image, category]

        item_keys = self.items.keys()
        del_keys = []
        for item_key in item_keys:
            if item_key not in item_names:
                del_keys.append(item_key)

        for del_key in del_keys:
            del self.items[del_key]


def draw_stats(agent, height, width, steps):
    ret = np.zeros((height, width, 3), dtype=np.uint8)
    
    # game info
    i = 0
    txt = [f'Level num: {agent.blstats.level_number}',
           f'Dung num: {agent.blstats.dungeon_number}',
           f'Step: {steps}',
           f'Turn: {0}',
           f'Score: {agent.blstats.score}',
           ]
    put_text(ret, ' | '.join(txt), (0, i * FONT_SIZE), color=(255, 255, 255))
    i += 3

    # general character info
    txt = [
        {v: k for k, v in name_to_role.items()}[agent.role],
        {v: k for k, v in name_to_race.items()}[agent.race],
        {v: k for k, v in name_to_alignment.items()}[agent.alignment],
        {v: k for k, v in name_to_gender.items()}[agent.gender],
    ]
    put_text(ret, ' | '.join(txt), (0, i * FONT_SIZE))
    i += 1
    txt = [f'HP: {agent.blstats.hitpoints} / {agent.blstats.max_hitpoints}',
           f'LVL: {agent.blstats.experience_level}',
           f'ENERGY: {agent.blstats.energy} / {agent.blstats.max_energy}',
           ]
    hp_ratio = agent.blstats.hitpoints / agent.blstats.max_hitpoints
    hp_color = cv2.applyColorMap(np.array([[130 - int((1 - hp_ratio) * 110)]], dtype=np.uint8),
                                 cv2.COLORMAP_TURBO)[0, 0]
    put_text(ret, ' | '.join(txt), (0, i * FONT_SIZE), color=tuple(map(int, hp_color)))
    i += 2
    '''
    # proficiency info
    colors = {
        'Basic': (100, 100, 255),
        'Skilled': (100, 255, 100),
        'Expert': (100, 255, 255),
        'Master': (255, 255, 100),
        'Grand Master': (255, 100, 100),
    }
    for line in ch.get_skill_str_list():
        if 'Unskilled' not in line:
            put_text(ret, line, (0, i * FONT_SIZE), color=colors[line.split('-')[-1]])
            i += 1

    unskilled = []
    for line in ch.get_skill_str_list():
        if 'Unskilled' in line:
            unskilled.append(line.split('-')[0])

    put_text(ret, '|'.join(unskilled), (0, i * FONT_SIZE), color=(100, 100, 100))
    i += 2
    put_text(ret, 'Unarmed bonus: ' + str(ch.get_melee_bonus(None)), (0, i * FONT_SIZE))
    i += 2

    stats = list(self.env.agent.stats_logger.get_stats_dict().items())
    stats = [(k, v) for k, v in stats if v != 0]
    for j in range((len(stats) + 2) // 3):
        def format_value(v):
            if isinstance(v, float):
                return f'{v:.2f}'
            return str(v)

        put_text(ret, ' | '.join(f'{k}={format_value(v)}' for k, v in stats[j * 3: (j + 1) * 3]),
                 (0, i * FONT_SIZE), color=(100, 100, 100))
        i += 1
    i += 1
    '''
    #if hasattr(self.env.agent.character, 'known_spells'):
    #    put_text(ret, 'Known spells: ' + str(list(self.env.agent.character.known_spells)), (0, i * FONT_SIZE))
    #    i += 1

    #monsters = [(dis, y, x, mon.mname) for dis, y, x, mon, _ in self.env.agent.get_visible_monsters()]
    #put_text(ret, 'Monsters: ' + str(monsters), (0, i * FONT_SIZE))
    draw_frame(ret)

    return ret


def draw_inventory(agent, last_obs, height, width):
    #width = 800
    vis = np.zeros((height, width, 3), dtype=np.uint8)
    tiles = []
    for i, item_key in enumerate(agent.items):
        # [name, letter, image, category]
        item = agent.items[item_key]

        name = item_key
        letter = item[0]
        image = item[1]
        category = item[2]

        matches = re.findall(
            r'^(a|an|the|\d+)'
            r'( empty)?'
            r'( (cursed|uncursed|blessed))?'
            r'( (very |thoroughly )?(rustproof|poisoned|corroded|rusty|burnt|rotted|partly eaten|partly used|diluted|unlocked|locked|wet|greased))*'
            r'( ([+-]\d+))? '
            r"([a-zA-z0-9-!'# ]+)"
            r'( \(([0-9]+:[0-9]+|no charge)\))?'
            r'( \(([a-zA-Z0-9; ]+(, flickering|, gleaming|, glimmering)?[a-zA-Z0-9; ]*)\))?'
            r'( \((for sale|unpaid), (\d+ aum, )?((\d+)[a-zA-Z- ]+|no charge)\))?'
            r'$',
            name)

        (
            count,
            effects1,
            _, status,
            effects2, _, _,
            _, modifier,
            name,
            _, uses,
            _, info, _,
            _, shop_status, _, _, shop_price
        ) = matches[0]

        item_vis = np.zeros((64, 800, 3), dtype=np.uint8)
        item_vis[:,0:64,:] = image
        cv2.putText(item_vis, name, (80, 50), cv2.FONT_HERSHEY_SIMPLEX, 1 * 0.7, (255, 255, 255), 1, cv2.LINE_AA)

        draw_frame(item_vis, color=(80, 80, 80), thickness=2)

        tiles.append(item_vis)

    if tiles:
        tiles_vis = np.concatenate(tiles, axis=0)

    vis[0:tiles_vis.shape[0], 0:tiles_vis.shape[1],: ] = tiles_vis

    draw_frame(vis)

    return vis