cmake_minimum_required(VERSION 3.16)
project(test_package LANGUAGES CXX)

find_package(Qt6 COMPONENTS Core Gui Quick Graphs QuickWidgets Widgets REQUIRED CONFIG)

add_executable(${PROJECT_NAME}
    main.cpp
    piewidget.h piewidget.cpp
    piegraph.h piegraph.cpp
)

target_link_libraries(${PROJECT_NAME} PRIVATE
    Qt6::Core
    Qt6::Gui
    Qt6::Quick
    Qt6::Graphs
    Qt6::QuickWidgets
    Qt6::Widgets
    Qt6::Quick
)

target_compile_features(${PROJECT_NAME} PRIVATE cxx_std_17)
set_target_properties(${PROJECT_NAME} PROPERTIES AUTOMOC ON AUTORCC ON)
