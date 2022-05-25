# RPG_RL
Playing the MMORPG using the Deep Reinforcement Learning. The Nethack and Diablo1 game will be used for environment.

# Reference
1. NetHack: https://github.com/facebookresearch/nle
2. NetHack Visualization: https://github.com/maciej-sypetkowski/autoascend
3. Diablo1 for Linux: https://github.com/diasurgical/devilutionX
4. Vizdoom: https://github.com/mwydmuch/ViZDoom
5. Simple SDL2 game: https://github.com/PolyMarsDev/Twini-Golf

# Detailed intruction for code
1. 

# NetHack
Visualization tool is added to original NLE of Facebook code.

<img src="image/vis_1.png" width="1000">

You can play a game yourself by below command.

```
$ python3.8 -m nle.scripts.play --env NetHackChallenge-v0
```

# Simple C++ SDL game
You can control the SDL2 C++ game using Python.

[![Python binding test for the golf game]([https://i3.ytimg.com/vi/fuBFcSBd8v8/hqdefault.jpg](https://img.youtube.com/vi/sEmLVRSOaHA/sddefault.jpg))](https://www.youtube.com/watch?v=sEmLVRSOaHA)

Move to [Twini-Golf folder](https://github.com/kimbring2/RPG_RL/tree/main/Twini-Golf) and build project using below command.

```
$ cmake .
$ make
```

Then, move to [lib_python folder](https://github.com/kimbring2/RPG_RL/tree/main/Twini-Golf/src/lib_python). You should check there is 'vizgolf.cpython-38-x86_64-linux-gnu.so' that was built. 

Open Jupyter Notebook for 'env_test.ipynb' and test code of video.
