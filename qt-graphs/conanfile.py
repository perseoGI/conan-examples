import os

from conan import ConanFile
from conan.tools.cmake import CMake, cmake_layout


class QtGraphsConan(ConanFile):
    settings = "os", "arch", "compiler", "build_type"
    generators = "CMakeDeps", "CMakeToolchain"

    def layout(self):
        cmake_layout(self)

    def requirements(self):
        self.requires(self.tested_reference_str, options={"qtgraphs": True, "qtquick3d": True})

    def build_requirements(self):
        self.tool_requires("cmake/[>=3.27 <4]")

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def test(self):
        bin_path = os.path.join(self.cpp.build.bindirs[0], "test_package")
        self.run(bin_path, env="conanrun")
