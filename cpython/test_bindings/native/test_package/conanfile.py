import os
from conan import ConanFile
from conan.tools.cmake import cmake_layout, CMake
from conan.tools.files import copy
from conan.tools.build import can_run
from conan.tools.microsoft import is_msvc
from conan.tools.cmake import CMakeDeps, CMakeToolchain

class CPythonTestBindingsNative(ConanFile):
    description = "A C++ application that embeds the Python interpreter."
    package_type = "application"
    settings = "os", "compiler", "build_type", "arch"

    def layout(self):
        cmake_layout(self)

    def requirements(self):
        self.requires(self.tested_reference_str)

    def generate(self):
        deps = CMakeDeps(self)
        deps.generate()
        tc = CMakeToolchain(self)
        tc.generate()

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def test(self):
        if can_run(self):
            # Test the C++ library
            bin_path = os.path.join(self.cpp.build.bindir, "test_package")
            self.run(bin_path, env="conanrun")

        # Test Python bindings if enabled
        if self.dependencies[self.tested_reference_str].options.get_safe("with_python", False):
            # Set PYTHONPATH to find the installed spam module
            spam_lib_path = os.path.join(self.dependencies[self.tested_reference_str].package_folder, "lib")
            
            self.output.info(f"Setting PYTHONPATH to: {spam_lib_path}")
            os.environ["PYTHONPATH"] = spam_lib_path
            
            self.output.info("Testing Python bindings for spam library")
            self.run(f"{self._python_exe} \"{self.source_folder}/test.py\"", env="conanrun")

    @property
    def _python_exe(self):
        return self.dependencies["cpython"].conf_info.get("user.cpython:python", check_type=str)

