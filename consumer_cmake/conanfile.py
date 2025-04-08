
from conan import ConanFile
from conan import ConanFile
from conan.tools.cmake import cmake_layout, CMake, CMakeDeps, CMakeToolchain

class ConsumerCmake(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    name = "consumer_cmake"
    version = "1.0"
    exports_sources = '*'

    def layout(self):
        cmake_layout(self)

    def requirements(self):
        self.requires("fmt/11.1.3")
        self.requires("libs/1.0")

    def generate(self):
        deps = CMakeDeps(self)
        deps.generate()
        tc = CMakeToolchain(self)
        tc.generate()

    def build(self):
        premake = CMake(self)
        premake.configure()
        premake.build()
