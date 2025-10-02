
from conan import ConanFile
from conan import ConanFile
from conan.tools.files import copy, chdir 
from conan.tools.layout import basic_layout
from conan.tools.premake import Premake, PremakeDeps, PremakeToolchain
import os

class Libs(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    name = "libs"
    version = "1.0"
    exports_sources = '*'
    package_type = "library"
    options = { "shared": [True, False] }
    default_options = { "shared": False }

    def layout(self):
        basic_layout(self)

    def requirements(self):
        self.requires("zstd/1.5.7")

    def generate(self):
        deps = PremakeDeps(self)
        deps.generate()
        tc = PremakeToolchain(self)
        tc.generate()

    def build(self):
        premake = Premake(self)
        premake.configure()
        premake.build(workspace="Libraries")

    def package(self):
        for lib in ["math", "utils"]:
            for header in ["*.h", "*.hpp"]:
                copy(self, header, os.path.join(self.source_folder, lib, "include"), os.path.join(self.package_folder, "include", "libs"))
            for lib in ("*.lib", "*.a", "*.dll", "*.so", "*.dylib"):
                copy(self, lib, os.path.join(self.build_folder, "bin"), os.path.join(self.package_folder, "lib"))

    def package_info(self):
        self.cpp_info.libs = ["math", "utils"]
