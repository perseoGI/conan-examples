include("conandeps.premake5.lua")

workspace "HelloWorld"
   location "../build-release"
   cppdialect "C++20"
   location "../build-release"
   targetdir  "../build-release"
   conan_setup()


-- workspace "HelloWorld"
--    location "../build-debug"
--    cppdialect "C++20"
--    location "../build-debug"
--    targetdir  "../build-debug"
--    conan_setup()


-- project "HelloWorld"
--    location "../build-release"
--    targetdir  "../build-release"


