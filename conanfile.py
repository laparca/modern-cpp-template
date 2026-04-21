from conan import ConanFile
from conan.tools.cmake import CMakeToolchain, CMakeDeps


class ProjectConan(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    requires = "gtest/1.17.0"

    def requirements(self):
        if self.settings.os == "Macos" and self.settings.compiler in ["apple-clang", "clang"]:
            self.requires("llvm-core/19.1.7")

    def generate(self):
        tc = CMakeToolchain(self)
        if self.settings.os == "Macos" and self.settings.compiler in ["apple-clang", "clang"]:
            llvm = self.dependencies["llvm-core"]
            tc.variables["CMAKE_C_COMPILER"] = f"{llvm.package_folder}/bin/clang"
            tc.variables["CMAKE_CXX_COMPILER"] = f"{llvm.package_folder}/bin/clang++"
        tc.generate()

        deps = CMakeDeps(self)
        deps.generate()
