from conan import ConanFile
from conan import ConanFile
from conan.tools.layout import basic_layout
from conan.tools.premake import Premake, PremakeDeps, PremakeToolchain

class ConsumerPremake(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    name = "consumer_premake"
    version = "1.0"
    exports_sources = '*'
    package_type = "application"

    def layout(self):
        basic_layout(self)

    def requirements(self):
        self.requires("libs/1.0")
        self.requires("spdlog/1.15.3")

    def generate(self):
        deps = PremakeDeps(self)
        deps.generate()
        tc = PremakeToolchain(self)
        tc.extra_defines = ["VALUE=2"]
        tc.extra_cflags = ["-Wextra"]
        tc.extra_cxxflags = ["-Wall", "-Wextra"]
        tc.extra_ldflags = ["-lm"]
        tc.project("main").extra_defines = ["TEST=False"]
        tc.project("test").disable = True
        tc.project("main").extra_cxxflags = ["-FS"]
        tc.generate()

    def build(self):
        premake = Premake(self)
        premake.configure()
        premake.build(workspace="App")
