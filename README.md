# Conan experimental examples

In this repository you can find some Conan special/new use cases which we are currently working on.


## Conan Config

### cmd_wrapper.py

This cmd_wrapper plugin allow running Conan test_package's binaries in cross compile environments using emulators!

For example, having a running Android emulator, you can run:


```sh 
conan create recipes/rapidyaml/all --version 0.10.0 -c tools.build.cross_building:can_run=True -pr android/static -b missing
```

And Conan will execute the test_package inside the emulator by copying the artifacts inside of it with `adb`:

```sh
======== Testing the package: Executing test ========
rapidyaml/0.10.0 (test package): Running test()
rapidyaml/0.10.0 (test package): RUN: bash -c '
        adb push ./test_package /data/local/tmp/test_package >/dev/null 2>&1
        adb shell chmod +x /data/local/tmp/test_package
        adb shell /data/local/tmp/test_package 
        code=$?
        adb shell rm -rf /data/local/tmp/*
        exit $code
    '
1
{foo: 1,bar: [bar0,bar1,bar2]}
```

This also works with shared builds

```sh 
conan create recipes/rapidyaml/all --version 0.10.0 -c tools.build.cross_building:can_run=True -pr android/static -o "*:shared=True" -b missing
```

In this case, the plugin will act as similarly to the `runtime_deploy` Conan's
deployer, copying all consumers shared libraries (when they are shared) to the
emulator.
Then, it will export the `LD_LIBRARY_PATH` environment variable, letting know the OS where to find the shared libraries:

```sh
======== Testing the package: Executing test ========
rapidyaml/0.10.0 (test package): Running test()
rapidyaml/0.10.0 (test package): RUN: bash -c '
        adb push ./test_package /data/local/tmp/test_package >/dev/null 2>&1
        adb shell mkdir -p /data/local/tmp/libs >/dev/null 2>&1
        adb push /Users/perseo/.conan2/p/b/rapidb7559cddc6217/p/lib/libryml.so /data/local/tmp/libs/libryml.so >/dev/null 2>&1
        adb push /Users/perseo/.conan2/p/b/c4cor4e8f05e6dbde9/p/lib/libc4core.so /data/local/tmp/libs/libc4core.so >/dev/null 2>&1
        adb shell chmod +x /data/local/tmp/test_package
        adb shell LD_LIBRARY_PATH=/data/local/tmp/libs /data/local/tmp/test_package 
        code=$?
        adb shell rm -rf /data/local/tmp/*
        exit $code
    '
1
{foo: 1,bar: [bar0,bar1,bar2]}
```

