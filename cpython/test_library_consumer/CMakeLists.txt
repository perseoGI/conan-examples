cmake_minimum_required(VERSION 3.15)
project(cpython-consumer CXX)

add_library(cpython-consumer src/mylib.cpp)
target_include_directories(cpython-consumer PUBLIC include)

set_target_properties(cpython-consumer PROPERTIES PUBLIC_HEADER "include/mylib.h")
install(TARGETS cpython-consumer)
