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
$ conan build consumer_cmake
```

Traces:
```
...
======== Calling build() ========
conanfile.py (consumer_cmake/1.0): Calling build()
conanfile.py (consumer_cmake/1.0): Running CMake.configure()
conanfile.py (consumer_cmake/1.0): RUN: cmake -G "Ninja" -DCMAKE_TOOLCHAIN_FILE="generators/conan_toolchain.cmake" -DCMAKE_INSTALL_PREFIX="/Use
rs/perseo/sources/conan-premake-example/consumer_cmake" -DCMAKE_POLICY_DEFAULT_CMP0091="NEW" -DCMAKE_BUILD_TYPE="Release" "/Users/perseo/source
s/conan-premake-example/consumer_cmake" --loglevel=VERBOSE
...
```

```
$ ./consumer_cmake/build/Release/consumer_cmake                               
PRINT: Hello World!
TEST_DEFINE is not defined
-2.3
-1
hello, 1, 2.3, 4.6, -1, -2.3
3
"hello"
(/ This is a test string
```


```sh
$ conan build consumer_premake
```

Traces:
```
...
======== Calling build() ========
conanfile.py (consumer_premake/1.0): Calling build()
luafile /Users/perseo/sources/conan-premake-example/consumer_premake/premake5.lua
conanfile.py (consumer_premake/1.0): RUN: premake5 --file=/Users/perseo/sources/conan-premake-example/consumer_premake/build-release/conanfile.
premake5.lua gmake --arch=arm64
Building configurations...
Running action 'gmake'...
Generated Makefile...
Generated main.make...
Done (14ms).

conanfile.py (consumer_premake/1.0): RUN: make config=release all -j
==== Building main (release) ====
Creating obj/Release
Creating bin
main.cpp
Linking main
...
```

```
$ ./consumer_premake/build-release/bin/main                               
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

- [ ] Link issues on shared libs on consumer side (consumer_cmake works well)

