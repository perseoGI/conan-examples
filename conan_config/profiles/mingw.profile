[settings]
os=Windows
arch=x86_64
compiler=gcc
compiler.version=13
compiler.libcxx=libstdc++11
build_type=Release
#compiler.exception=sjlj
compiler.threads=posix

[conf]
tools.build:compiler_executables={"c":"/urs/bin/x86_64-w64-mingw32-gcc", "cpp":"/urs/bin/x86_64-w64-mingw32-g++", "rc":"/urs/bin/x86_64-w64-mingw32-windres"}
