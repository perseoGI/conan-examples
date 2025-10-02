cmake_minimum_required(VERSION 3.15)
project(test_package CXX)

find_package(Python3 REQUIRED COMPONENTS Interpreter Development.Embed)

add_executable(${PROJECT_NAME} "test_package.cpp")
target_link_libraries(${PROJECT_NAME} PRIVATE Python3::Python)

