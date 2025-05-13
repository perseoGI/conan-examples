workspace "App"
   configurations { "Debug", "Release" }
   defines { "TEST=1", "VALUE=0" }

project "main"
   kind "ConsoleApp"
   language "C++"
   cppdialect "C++17"
   defines { "VALUE=1" }
   files { "src/main.cpp", } 
   
   filter "configurations:Debug"
      defines { "DEBUG" }
      symbols "On"

   filter "configurations:Release"
      defines { "NDEBUG" }
      optimize "On"

project "other"
   kind "ConsoleApp"
   language "C"

   files { "src/other.c" }

   filter "configurations:Debug"
      defines { "DEBUG" }
      symbols "On"

   filter "configurations:Release"
      defines { "NDEBUG" }
      optimize "On"

project "test"
   kind "ConsoleApp"
   language "C++"

   files { "src/test.cpp" }

   filter "configurations:Debug"
      defines { "DEBUG" }
      symbols "On"

   filter "configurations:Release"
      defines { "NDEBUG" }
      optimize "On"
