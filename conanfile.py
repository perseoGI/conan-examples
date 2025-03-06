
from conan import ConanFile
from conan import ConanFile
from conan.tools.files import copy, chdir 
from conan.tools.layout import basic_layout
from conan.tools.premake import Premake, PremakeDeps, PremakeToolchain
import os

class Pkg(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    name = "pkg"
    version = "1.0"
    exports_sources = '*'

    def layout(self):
        basic_layout(self, src_folder="src")

    def requirements(self):
        self.requires("fmt/11.1.3")

    def generate(self):
        deps = PremakeDeps(self)
        deps.generate()
        tc = PremakeToolchain(self, workspace="*")
        tc.variables["TEST"] = False
        # tc.projects["HelloWorld"].kind = "ConsoleApp"
        tc.generate()

    def build(self):
        with chdir(self, self.source_folder):
            premake = Premake(self)
            premake.configure()
        if self.settings.os != "Windows":
            build_type = str(self.settings.build_type)
            self.run(f"make config={build_type.lower()} -j")

    def package(self):
        copy(self, "*.h", os.path.join(self.source_folder, "include"), os.path.join(self.package_folder, "include", "pkg"))
        for lib in ("*.lib", "*.a"):
            copy(self, lib, self.source_folder, os.path.join(self.package_folder, "lib"), keep_path=False)
