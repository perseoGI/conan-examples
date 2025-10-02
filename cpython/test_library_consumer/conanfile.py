from conan import ConanFile
from conan.tools.cmake import CMake, CMakeToolchain, cmake_layout
import os


class CPythonConsumerConan(ConanFile):
    name = "cpython-consumer"
    version = "0.1"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = {"shared": False}
    exports_sources = "CMakeLists.txt", "src/*", "include/*", "myscript.py"

    def layout(self):
        cmake_layout(self)

    def build_requirements(self):
        self.tool_requires("cpython/3.13.7")

    def generate(self):
        tc = CMakeToolchain(self)
        tc.generate()

    def build(self):
        python_exe = self.dependencies.build["cpython"].conf_info.get("user.cpython:python")
        self.run(f'"{python_exe}" {os.path.join(self.source_folder, "myscript.py")}')

        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        cmake = CMake(self)
        cmake.install()

    def package_info(self):
        self.cpp_info.libs = ["cpython-consumer"]
