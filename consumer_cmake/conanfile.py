
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
        self.requires("libs/1.0")
        self.requires("spdlog/1.15.3")
        self.requires("icu/74.2")

    def generate(self):
        deps = CMakeDeps(self)
        deps.generate()
        tc = CMakeToolchain(self)
        tc.blocks["rpath"].skip_rpath = True
        tc.generate()

    def build(self):
        premake = CMake(self)
        premake.configure()
        premake.build()
