# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.23

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:

#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:

# Disable VCS-based implicit rules.
% : %,v

# Disable VCS-based implicit rules.
% : RCS/%

# Disable VCS-based implicit rules.
% : RCS/%,v

# Disable VCS-based implicit rules.
% : SCCS/s.%

# Disable VCS-based implicit rules.
% : s.%

.SUFFIXES: .hpux_make_needs_suffix_list

# Command-line flag to silence nested $(MAKE).
$(VERBOSE)MAKESILENT = -s

#Suppress display of executed commands.
$(VERBOSE).SILENT:

# A target that is always out of date.
cmake_force:
.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E rm -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/kimbring2/Twini-Golf

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/kimbring2/Twini-Golf

# Include any dependencies generated for this target.
include CMakeFiles/libvizgolf_shared.dir/depend.make
# Include any dependencies generated by the compiler for this target.
include CMakeFiles/libvizgolf_shared.dir/compiler_depend.make

# Include the progress variables for this target.
include CMakeFiles/libvizgolf_shared.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/libvizgolf_shared.dir/flags.make

CMakeFiles/libvizgolf_shared.dir/src/lib/ViZGolfController.cpp.o: CMakeFiles/libvizgolf_shared.dir/flags.make
CMakeFiles/libvizgolf_shared.dir/src/lib/ViZGolfController.cpp.o: src/lib/ViZGolfController.cpp
CMakeFiles/libvizgolf_shared.dir/src/lib/ViZGolfController.cpp.o: CMakeFiles/libvizgolf_shared.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/kimbring2/Twini-Golf/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object CMakeFiles/libvizgolf_shared.dir/src/lib/ViZGolfController.cpp.o"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -MD -MT CMakeFiles/libvizgolf_shared.dir/src/lib/ViZGolfController.cpp.o -MF CMakeFiles/libvizgolf_shared.dir/src/lib/ViZGolfController.cpp.o.d -o CMakeFiles/libvizgolf_shared.dir/src/lib/ViZGolfController.cpp.o -c /home/kimbring2/Twini-Golf/src/lib/ViZGolfController.cpp

CMakeFiles/libvizgolf_shared.dir/src/lib/ViZGolfController.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/libvizgolf_shared.dir/src/lib/ViZGolfController.cpp.i"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/kimbring2/Twini-Golf/src/lib/ViZGolfController.cpp > CMakeFiles/libvizgolf_shared.dir/src/lib/ViZGolfController.cpp.i

CMakeFiles/libvizgolf_shared.dir/src/lib/ViZGolfController.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/libvizgolf_shared.dir/src/lib/ViZGolfController.cpp.s"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/kimbring2/Twini-Golf/src/lib/ViZGolfController.cpp -o CMakeFiles/libvizgolf_shared.dir/src/lib/ViZGolfController.cpp.s

CMakeFiles/libvizgolf_shared.dir/src/lib/ViZGolfExceptions.cpp.o: CMakeFiles/libvizgolf_shared.dir/flags.make
CMakeFiles/libvizgolf_shared.dir/src/lib/ViZGolfExceptions.cpp.o: src/lib/ViZGolfExceptions.cpp
CMakeFiles/libvizgolf_shared.dir/src/lib/ViZGolfExceptions.cpp.o: CMakeFiles/libvizgolf_shared.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/kimbring2/Twini-Golf/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Building CXX object CMakeFiles/libvizgolf_shared.dir/src/lib/ViZGolfExceptions.cpp.o"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -MD -MT CMakeFiles/libvizgolf_shared.dir/src/lib/ViZGolfExceptions.cpp.o -MF CMakeFiles/libvizgolf_shared.dir/src/lib/ViZGolfExceptions.cpp.o.d -o CMakeFiles/libvizgolf_shared.dir/src/lib/ViZGolfExceptions.cpp.o -c /home/kimbring2/Twini-Golf/src/lib/ViZGolfExceptions.cpp

CMakeFiles/libvizgolf_shared.dir/src/lib/ViZGolfExceptions.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/libvizgolf_shared.dir/src/lib/ViZGolfExceptions.cpp.i"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/kimbring2/Twini-Golf/src/lib/ViZGolfExceptions.cpp > CMakeFiles/libvizgolf_shared.dir/src/lib/ViZGolfExceptions.cpp.i

CMakeFiles/libvizgolf_shared.dir/src/lib/ViZGolfExceptions.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/libvizgolf_shared.dir/src/lib/ViZGolfExceptions.cpp.s"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/kimbring2/Twini-Golf/src/lib/ViZGolfExceptions.cpp -o CMakeFiles/libvizgolf_shared.dir/src/lib/ViZGolfExceptions.cpp.s

CMakeFiles/libvizgolf_shared.dir/src/lib/ViZGolfGame.cpp.o: CMakeFiles/libvizgolf_shared.dir/flags.make
CMakeFiles/libvizgolf_shared.dir/src/lib/ViZGolfGame.cpp.o: src/lib/ViZGolfGame.cpp
CMakeFiles/libvizgolf_shared.dir/src/lib/ViZGolfGame.cpp.o: CMakeFiles/libvizgolf_shared.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/kimbring2/Twini-Golf/CMakeFiles --progress-num=$(CMAKE_PROGRESS_3) "Building CXX object CMakeFiles/libvizgolf_shared.dir/src/lib/ViZGolfGame.cpp.o"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -MD -MT CMakeFiles/libvizgolf_shared.dir/src/lib/ViZGolfGame.cpp.o -MF CMakeFiles/libvizgolf_shared.dir/src/lib/ViZGolfGame.cpp.o.d -o CMakeFiles/libvizgolf_shared.dir/src/lib/ViZGolfGame.cpp.o -c /home/kimbring2/Twini-Golf/src/lib/ViZGolfGame.cpp

CMakeFiles/libvizgolf_shared.dir/src/lib/ViZGolfGame.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/libvizgolf_shared.dir/src/lib/ViZGolfGame.cpp.i"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/kimbring2/Twini-Golf/src/lib/ViZGolfGame.cpp > CMakeFiles/libvizgolf_shared.dir/src/lib/ViZGolfGame.cpp.i

CMakeFiles/libvizgolf_shared.dir/src/lib/ViZGolfGame.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/libvizgolf_shared.dir/src/lib/ViZGolfGame.cpp.s"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/kimbring2/Twini-Golf/src/lib/ViZGolfGame.cpp -o CMakeFiles/libvizgolf_shared.dir/src/lib/ViZGolfGame.cpp.s

CMakeFiles/libvizgolf_shared.dir/src/lib/ViZGolfMessageQueue.cpp.o: CMakeFiles/libvizgolf_shared.dir/flags.make
CMakeFiles/libvizgolf_shared.dir/src/lib/ViZGolfMessageQueue.cpp.o: src/lib/ViZGolfMessageQueue.cpp
CMakeFiles/libvizgolf_shared.dir/src/lib/ViZGolfMessageQueue.cpp.o: CMakeFiles/libvizgolf_shared.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/kimbring2/Twini-Golf/CMakeFiles --progress-num=$(CMAKE_PROGRESS_4) "Building CXX object CMakeFiles/libvizgolf_shared.dir/src/lib/ViZGolfMessageQueue.cpp.o"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -MD -MT CMakeFiles/libvizgolf_shared.dir/src/lib/ViZGolfMessageQueue.cpp.o -MF CMakeFiles/libvizgolf_shared.dir/src/lib/ViZGolfMessageQueue.cpp.o.d -o CMakeFiles/libvizgolf_shared.dir/src/lib/ViZGolfMessageQueue.cpp.o -c /home/kimbring2/Twini-Golf/src/lib/ViZGolfMessageQueue.cpp

CMakeFiles/libvizgolf_shared.dir/src/lib/ViZGolfMessageQueue.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/libvizgolf_shared.dir/src/lib/ViZGolfMessageQueue.cpp.i"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/kimbring2/Twini-Golf/src/lib/ViZGolfMessageQueue.cpp > CMakeFiles/libvizgolf_shared.dir/src/lib/ViZGolfMessageQueue.cpp.i

CMakeFiles/libvizgolf_shared.dir/src/lib/ViZGolfMessageQueue.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/libvizgolf_shared.dir/src/lib/ViZGolfMessageQueue.cpp.s"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/kimbring2/Twini-Golf/src/lib/ViZGolfMessageQueue.cpp -o CMakeFiles/libvizgolf_shared.dir/src/lib/ViZGolfMessageQueue.cpp.s

CMakeFiles/libvizgolf_shared.dir/src/lib/ViZGolfSharedMemory.cpp.o: CMakeFiles/libvizgolf_shared.dir/flags.make
CMakeFiles/libvizgolf_shared.dir/src/lib/ViZGolfSharedMemory.cpp.o: src/lib/ViZGolfSharedMemory.cpp
CMakeFiles/libvizgolf_shared.dir/src/lib/ViZGolfSharedMemory.cpp.o: CMakeFiles/libvizgolf_shared.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/kimbring2/Twini-Golf/CMakeFiles --progress-num=$(CMAKE_PROGRESS_5) "Building CXX object CMakeFiles/libvizgolf_shared.dir/src/lib/ViZGolfSharedMemory.cpp.o"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -MD -MT CMakeFiles/libvizgolf_shared.dir/src/lib/ViZGolfSharedMemory.cpp.o -MF CMakeFiles/libvizgolf_shared.dir/src/lib/ViZGolfSharedMemory.cpp.o.d -o CMakeFiles/libvizgolf_shared.dir/src/lib/ViZGolfSharedMemory.cpp.o -c /home/kimbring2/Twini-Golf/src/lib/ViZGolfSharedMemory.cpp

CMakeFiles/libvizgolf_shared.dir/src/lib/ViZGolfSharedMemory.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/libvizgolf_shared.dir/src/lib/ViZGolfSharedMemory.cpp.i"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/kimbring2/Twini-Golf/src/lib/ViZGolfSharedMemory.cpp > CMakeFiles/libvizgolf_shared.dir/src/lib/ViZGolfSharedMemory.cpp.i

CMakeFiles/libvizgolf_shared.dir/src/lib/ViZGolfSharedMemory.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/libvizgolf_shared.dir/src/lib/ViZGolfSharedMemory.cpp.s"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/kimbring2/Twini-Golf/src/lib/ViZGolfSharedMemory.cpp -o CMakeFiles/libvizgolf_shared.dir/src/lib/ViZGolfSharedMemory.cpp.s

# Object files for target libvizgolf_shared
libvizgolf_shared_OBJECTS = \
"CMakeFiles/libvizgolf_shared.dir/src/lib/ViZGolfController.cpp.o" \
"CMakeFiles/libvizgolf_shared.dir/src/lib/ViZGolfExceptions.cpp.o" \
"CMakeFiles/libvizgolf_shared.dir/src/lib/ViZGolfGame.cpp.o" \
"CMakeFiles/libvizgolf_shared.dir/src/lib/ViZGolfMessageQueue.cpp.o" \
"CMakeFiles/libvizgolf_shared.dir/src/lib/ViZGolfSharedMemory.cpp.o"

# External object files for target libvizgolf_shared
libvizgolf_shared_EXTERNAL_OBJECTS =

LIBRARY_OUTPUT_DIRECTORY_RELEASE/libvizgolf.so: CMakeFiles/libvizgolf_shared.dir/src/lib/ViZGolfController.cpp.o
LIBRARY_OUTPUT_DIRECTORY_RELEASE/libvizgolf.so: CMakeFiles/libvizgolf_shared.dir/src/lib/ViZGolfExceptions.cpp.o
LIBRARY_OUTPUT_DIRECTORY_RELEASE/libvizgolf.so: CMakeFiles/libvizgolf_shared.dir/src/lib/ViZGolfGame.cpp.o
LIBRARY_OUTPUT_DIRECTORY_RELEASE/libvizgolf.so: CMakeFiles/libvizgolf_shared.dir/src/lib/ViZGolfMessageQueue.cpp.o
LIBRARY_OUTPUT_DIRECTORY_RELEASE/libvizgolf.so: CMakeFiles/libvizgolf_shared.dir/src/lib/ViZGolfSharedMemory.cpp.o
LIBRARY_OUTPUT_DIRECTORY_RELEASE/libvizgolf.so: CMakeFiles/libvizgolf_shared.dir/build.make
LIBRARY_OUTPUT_DIRECTORY_RELEASE/libvizgolf.so: CMakeFiles/libvizgolf_shared.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/kimbring2/Twini-Golf/CMakeFiles --progress-num=$(CMAKE_PROGRESS_6) "Linking CXX shared library LIBRARY_OUTPUT_DIRECTORY_RELEASE/libvizgolf.so"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/libvizgolf_shared.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/libvizgolf_shared.dir/build: LIBRARY_OUTPUT_DIRECTORY_RELEASE/libvizgolf.so
.PHONY : CMakeFiles/libvizgolf_shared.dir/build

CMakeFiles/libvizgolf_shared.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/libvizgolf_shared.dir/cmake_clean.cmake
.PHONY : CMakeFiles/libvizgolf_shared.dir/clean

CMakeFiles/libvizgolf_shared.dir/depend:
	cd /home/kimbring2/Twini-Golf && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/kimbring2/Twini-Golf /home/kimbring2/Twini-Golf /home/kimbring2/Twini-Golf /home/kimbring2/Twini-Golf /home/kimbring2/Twini-Golf/CMakeFiles/libvizgolf_shared.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/libvizgolf_shared.dir/depend

