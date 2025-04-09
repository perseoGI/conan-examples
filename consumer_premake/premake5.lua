workspace "App"
   configurations { "Debug", "Release" }
   defines { "TEST=1" }

project "main"
   kind "ConsoleApp"
   language "C++"
   cppdialect "C++17"

   files { "**.h", "**.cpp" } 
   
   filter "configurations:Debug"
      defines { "DEBUG" }
      symbols "On"

   filter "configurations:Release"
      defines { "NDEBUG" }
      optimize "On"

