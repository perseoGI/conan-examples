# cmake_minimum_required(VERSION 3.15)
# project(test_package C)
#
# find_package(Python3 REQUIRED COMPONENTS Interpreter Development.Module Development.Embed)
#
# message("Python3_EXECUTABLE: ${Python3_EXECUTABLE}")
# message("Python3_INTERPRETER_ID: ${Python3_INTERPRETER_ID}")
# message("Python3_VERSION: ${Python3_VERSION}")
# message("Python3_INCLUDE_DIRS: ${Python3_INCLUDE_DIRS}")
# message("Python3_LIBRARIES: ${Python3_LIBRARIES}")
#
# option(BUILD_MODULE "Build python module")
# if(BUILD_MODULE)
#     python3_add_library(spam "test_module.c")
#     if(MSVC)
#         set_target_properties(spam PROPERTIES DEBUG_POSTFIX "_d")
#     endif()
# endif()
#


cmake_minimum_required(VERSION 3.15)
project(cpython-bindings-native CXX C)

# Build the C++ library
add_library(cpython-bindings-native src/spam.cpp)
target_include_directories(cpython-bindings-native PUBLIC include)

set_target_properties(cpython-bindings-native PROPERTIES PUBLIC_HEADER "include/spam.h")
install(TARGETS cpython-bindings-native)

# Option to build Python bindings (controlled by Conan)
option(BUILD_MODULE "Build python extension module" OFF)

if(BUILD_MODULE)
    find_package(Python3 REQUIRED COMPONENTS Interpreter Development.Module)

    message(STATUS "Python3_EXECUTABLE: ${Python3_EXECUTABLE}")
    message(STATUS "Python3_VERSION: ${Python3_VERSION}")
    message(STATUS "Python3_INCLUDE_DIRS: ${Python3_INCLUDE_DIRS}")
    message(STATUS "Python3_LIBRARIES: ${Python3_LIBRARIES}")

    python3_add_library(spam MODULE bindings/spam_bindings.cpp)

    target_include_directories(spam PRIVATE ${Python3_INCLUDE_DIRS})
    target_link_libraries(spam PRIVATE ${Python3_LIBRARIES})
    
    # Link with our C++ library if needed
    target_link_libraries(spam PRIVATE cpython-bindings-native)

    if(MSVC)
        set_target_properties(spam PROPERTIES DEBUG_POSTFIX "_d")
    endif()
    
    # Install the Python module
    install(TARGETS spam DESTINATION lib)
endif()











# cmake_minimum_required(VERSION 3.15)
# project(test_package C)
#
# find_package(Python3 REQUIRED COMPONENTS Interpreter Development.Module Development.Embed)
#
# message("Python3_EXECUTABLE: ${Python3_EXECUTABLE}")
# message("Python3_INTERPRETER_ID: ${Python3_INTERPRETER_ID}")
# message("Python3_VERSION: ${Python3_VERSION}")
# message("Python3_INCLUDE_DIRS: ${Python3_INCLUDE_DIRS}")
# message("Python3_LIBRARIES: ${Python3_LIBRARIES}")
#
# option(BUILD_MODULE "Build python module")
# if(BUILD_MODULE)
#     python3_add_library(spam "test_module.c")
#     if(MSVC)
#         set_target_properties(spam PROPERTIES DEBUG_POSTFIX "_d")
#     endif()
# endif()
