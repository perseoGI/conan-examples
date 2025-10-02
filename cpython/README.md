# Conan and CPython recipe example

This repository contains fictitious consumer recipes designed to demonstrate complete and representative usage patterns with Conan and `CPython`.

* A "library"-style recipe with a `shared` option (True/False), which uses a tool_requires on CPython to run a script either at CMake build time.
* A "library"-style recipe with a `shared` option (True/False) and an additional `with_python` option that builds Python bindings.
  Several approaches are included:
  * Hardcoded C bindings, using CMake’s built-in FindPython.
  * Bindings built with PyBind11 + FindPython.
  * Bindings built with Swig 4.x + FindPython.
* An "application"-style recipe embedding the Python interpreter (with a regular requires in the host context).
