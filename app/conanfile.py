
from conan import ConanFile
from conan import ConanFile
from conan.tools.files import copy, chdir 
from conan.tools.layout import basic_layout
from conan.tools.premake import Premake, PremakeDeps, PremakeToolchain
import os

class App(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    name = "app"
    version = "1.0"
    exports_sources = '*'

    def layout(self):
        basic_layout(self)

    def requirements(self):
        self.requires("fmt/11.1.3")
        self.requires("libs/1.0")

    def generate(self):
        deps = PremakeDeps(self)
        deps.generate()
        tc = PremakeToolchain(self)
        tc.defines["TEST"] = False
        tc.generate()

    def build(self):
        premake = Premake(self)
        premake.configure()
        premake.build()
