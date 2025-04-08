cmake_minimum_required(VERSION 3.15)
project(consumer_cmake CXX)

add_executable(consumer_cmake src/main.cpp)

find_package(fmt)
find_package(libs)
target_link_libraries(consumer_cmake PRIVATE libs::libs fmt::fmt)

install(TARGETS consumer_cmake DESTINATION "."
        RUNTIME DESTINATION bin
        ARCHIVE DESTINATION lib
        LIBRARY DESTINATION lib
        )
