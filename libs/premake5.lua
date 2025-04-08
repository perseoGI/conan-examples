workspace "Libraries"
    configurations { "Debug", "Release" }
    fatalwarnings {"All"}
    floatingpoint "Fast"
    includedirs { ".", "math", "utils" }


project "math"
    cppdialect "C++17"
    kind "StaticLib"
    language "C++"
    files { "math/include/math.hpp", "math/src/math.cpp" }

project "utils"
    cppdialect "C++17"
    -- kind "StaticLib"
    kind "SharedLib"
    language "C++"
    files { "utils/include/*.hpp", "utils/include/*.h", "utils/src/*.cpp" }
