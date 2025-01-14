set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++14 -O3 -Wall -m64 -I include")

file(GLOB twingolf_SRC
     "src/*.h"
     "src/*.cpp"
)

find_package(SDL2 REQUIRED)
include_directories(${SDL2_INCLUDE_DIRS})

# always
FIND_PACKAGE(Threads REQUIRED)

# if using boost
SET(Boost_USE_MULTITHREADED ON)

set(prefix "/usr")
set(exec_prefix "${prefix}")
set(libdir "/usr/lib64")
set(SDL2_PREFIX "/usr")
set(SDL2_EXEC_PREFIX "/usr")
set(SDL2_LIBDIR "/usr/lib64")
set(SDL2_INCLUDE_DIRS "${prefix}/include/SDL2")
set(SDL2_LIBRARIES "-L${SDL2_LIBDIR} -lSDL2 -lSDL2_image -lSDL2_ttf -lSDL2_mixer")
string(STRIP "${SDL2_LIBRARIES}" SDL2_LIBRARIES)

add_executable(twingolf ${twingolf_SRC})
target_link_libraries(twingolf ${SDL2_LIBRARIES} rt ${OpenCV_LIBS} ${Boost_LIBRARIES} ${CMAKE_THREAD_LIBS_INIT})