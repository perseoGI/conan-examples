# Conan premake integration example


For this project to run successfully, a conan fork is needed (currently) 

Follow Conan PR in https://github.com/conan-io/conan/pull/17898
Follow Premake discussion in https://github.com/premake/premake-core/discussions/2441


This example aims to test:

* Packaging of a premake5 library with multiple libs with conan without modifying any build script from source code
* Packaging libs shared and static
* Using conan to compile a premake5 application depending on CCI dependencies and on previous library packaged

### Compilation


```sh
$ conan create libs --build=missing
```
Traces:
```
...

libs/1.0: Calling build()
libs/1.0: RUN: premake5 --file=/Users/perseo/.conan2/p/b/libscd427d168f28b/b/build-release/conanfile.premake5.lua gmake --scripts=/Users/perseo/.conan2/p/b/libscd427d168f28b/b/build-release/conan --arch=arm64
Building configurations...
Running action 'gmake'...
Generated Makefile...
Generated math.make...
Generated utils.make...
Done (21ms).

libs/1.0: RUN: make config=release -j
==== Building math (release) ====
==== Building utils (release) ====
Creating obj/Release/math
Creating obj/Release/utils
math.cpp
compression.cpp
quote.cpp
Linking math
Linking utils
...

```


```sh
$ conan build app --build=missing
```

Traces:
```
...

======== Calling build() ========
conanfile.py (app/1.0): Calling build()
conanfile.py (app/1.0): RUN: premake5 --file=/Users/perseo/sources/test/premake-conan/app/build-release/conanfile.premake5.lua gmake --scripts=/Users/perseo/sources/test/premake-conan/app/build-release/conan --arch=arm64
Building configurations...
Running action 'gmake'...
Generated Makefile...
Generated main.make...
Done (22ms).

conanfile.py (app/1.0): RUN: make config=release -j
==== Building main (release) ====
Creating obj/Release
main.cpp
Linking main

...
```

```
$ ./app/build-release/main
PRINT: Hello World!
TEST_DEFINE is not defined
-2.3
-1
hello, 1, 2.3, 4.6, -1, -2.3
3
"hello"
(/ This is a test string
```


### Progress

#### Things to be done in Premake side (if possible)

- [ ] Configure libs to be build shared or static from toolchain -> similar to CMake BUILD_SHARED_LIBS
- [ ] Unset previously defines added in premake5.lua from toolchain by modifyinj global workspace

#### TODOs on conan generator side

- [ ] Premake should work without declaring premakedeps or premaketoolchain

