workspace "Libraries"
    configurations { "Debug", "Release", "Debug Sanitizers", "Release Sanitizers" }
    fatalwarnings {"All"}
    floatingpoint "Fast"
    includedirs { ".", "math", "utils" }

    filter { "configurations:Debug Sanitizers" }
        defines { "SANITIZERS" }
        symbols "On"
        optimize "Off"
    filter{}

project "math"
    cppdialect "C++17"
    -- kind "StaticLib"
    language "C++"
    files { "math/include/math.hpp", "math/src/math.cpp" }

project "utils"
    cppdialect "C++17"
    -- kind "StaticLib"
    -- kind "SharedLib" -- Fail to consume
                        -- dyld[67347]: Library not loaded: @rpath/libutils.dylib
                        --   Referenced from: <0D3A9E16-82B5-3338-9F73-DBDE0829870D> /Users/perseo/sources/conan-premake-example/consumer_premake/build-release/bin/main
                        --   Reason: no LC_RPATH's found
                        -- [1]    67347 abort      ./consumer_premake/build-release/bin/main
    language "C++"
    files { "utils/include/*.hpp", "utils/include/*.h", "utils/src/*.cpp" }

premake.override(premake.modules.gmake, "target", function(base, cfg, toolset)
  local targetpath = string.gsub(premake.project.getrelative(cfg.project, cfg.buildtarget.directory), ' ', '_')
  premake.outln('TARGETDIR = ' .. targetpath)
  premake.outln('TARGET = $(TARGETDIR)/' .. cfg.buildtarget.name)
end)
  
premake.override(premake.modules.gmake, "objdir", function(base, cfg, toolset)
  local objpath = string.gsub(premake.project.getrelative(cfg.project, cfg.objdir), ' ', '_')
  premake.outln('OBJDIR = ' .. objpath)
end)
