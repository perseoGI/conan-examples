import os
from conan import ConanFile
from conan.tools.cmake import cmake_layout, CMake
from conan.tools.files import copy
from conan.tools.microsoft import is_msvc
from conan.tools.cmake import CMakeDeps, CMakeToolchain
from pathlib import Path

class CPythonBindingsNative(ConanFile):
    name = "cpython-bindings-native"
    description = "A C++ application that embeds the Python interpreter."
    version = "0.1"
    package_type = "library"
    settings = "os", "compiler", "build_type", "arch"
    options = {
        "shared": [True, False],
        "with_python": [True, False],
    }
    default_options = {
        "shared": False,
        "with_python": True
    }
    exports_sources = "CMakeLists.txt", "src/*", "include/*", "bindings/*"

    def _cpython_option(self, name):
        return self.dependencies["cpython"].options.get_safe(name, False)

    @property
    def _support_py_bindings(self):
        return not (is_msvc(self) or self.dependencies["cpython"].options.get_safe("shared", False))

    @property
    def _python_exe(self):
        return self.dependencies["cpython"].conf_info.get("user.cpython:python", check_type=str)

    def layout(self):
        cmake_layout(self)

    def config_options(self):
        if self.settings.os == "Windows":
            del self.options.shared
        if not self._support_py_bindings:
            del self.options.with_python

    def requirements(self):
        if self.options.get_safe("with_python", False):
            self.requires("cpython/3.13.7")

    def generate(self):
        deps = CMakeDeps(self)
        deps.generate()
        tc = CMakeToolchain(self)
        if self.options.with_python:
            tc.cache_variables["BUILD_MODULE"] = True
            tc.cache_variables["Python_EXECUTABLE"] = self._python_exe
        tc.generate()

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        cmake = CMake(self)
        cmake.install()

    def package_info(self):
        self.cpp_info.libs = ["cpython-bindings-native"]
