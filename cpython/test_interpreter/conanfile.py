import os
from conan import ConanFile
from conan.tools.cmake import cmake_layout, CMake
from conan.tools.files import copy

class CPythonTestInterpreter(ConanFile):
    description = "A C++ application that embeds the Python interpreter."
    package_type = "application"
    settings = "os", "compiler", "build_type", "arch"
    generators = "CMakeDeps", "CMakeToolchain"

    def layout(self):
        cmake_layout(self)

    def requirements(self):
        self.requires(self.tested_reference_str)

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def test(self):
        copy(self, "embedded_script.py", self.source_folder, self.cpp.build.bindir)
        bin_path = os.path.join(self.cpp.build.bindir, "test_package")
        self.run(bin_path, env="conanrun")
