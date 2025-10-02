#include <Python.h>
#include <iostream>

// Helper function to handle Python errors
void handle_python_error() {
  if (PyErr_Occurred()) {
    PyErr_Print();
    PyObject *ptype, *pvalue, *ptraceback;
    PyErr_Fetch(&ptype, &pvalue, &ptraceback);
    if (pvalue) {
      PyObject *pStr = PyObject_Str(pvalue);
      if (pStr) {
        std::cerr << "Python error: " << PyUnicode_AsUTF8(pStr) << std::endl;
        Py_DECREF(pStr);
      }
    }
    Py_XDECREF(ptype);
    Py_XDECREF(pvalue);
    Py_XDECREF(ptraceback);
    throw std::runtime_error("Python execution failed.");
  }
}

int main(int argc, char *argv[]) {
  // Initialize the Python interpreter. This must be called before using any
  // other Python C API function.
  Py_Initialize();

  if (!Py_IsInitialized()) {
    std::cerr << "Failed to initialize Python interpreter!" << std::endl;
    return 1;
  }
  std::cout << "Python interpreter initialized successfully." << std::endl;

  try {
    // Add the current directory to Python's search path, so we can import our
    // script. The working directory must be the `bin` folder where the
    // executable and script are located.
    PyRun_SimpleString("import sys");
    PyRun_SimpleString("sys.path.append('.')");

    // Import the Python module.
    PyObject *pName = PyUnicode_DecodeFSDefault("embedded_script");
    PyObject *pModule = PyImport_Import(pName);
    Py_DECREF(pName);

    if (!pModule) {
      PyErr_Print();
      std::cerr << "Failed to import Python module 'embedded_script'."
                << std::endl;
      Py_Finalize();
      return 1;
    }

    // Call a void function
    // Get a reference to the 'say_hello' function.
    PyObject *pFunc = PyObject_GetAttrString(pModule, "say_hello");
    if (!pFunc || !PyCallable_Check(pFunc)) {
      if (PyErr_Occurred())
        PyErr_Print();
      std::cerr << "Cannot find callable function 'say_hello'." << std::endl;
      Py_DECREF(pModule);
      Py_Finalize();
      return 1;
    }

    // Call the function. We don't need to pass any arguments.
    PyObject *pValue = PyObject_CallObject(pFunc, NULL);
    if (!pValue) {
      PyErr_Print();
      std::cerr << "Call to 'say_hello' failed." << std::endl;
    }

    // Get a reference to the 'fibonacci' function.
    pFunc = PyObject_GetAttrString(pModule, "fibonacci");
    if (!pFunc || !PyCallable_Check(pFunc)) {
      Py_XDECREF(pFunc);
      Py_DECREF(pModule);
      throw std::runtime_error("Cannot find callable function 'fibonacci'.");
    }

    // --- Call the Python function with an argument ---
    long long n = 10;
    PyObject *pArgs = Py_BuildValue(
        "(L)", n); // Create a Python tuple with one long long argument
    if (!pArgs) {
      Py_DECREF(pFunc);
      Py_DECREF(pModule);
      throw std::runtime_error("Failed to create Python arguments.");
    }

    pValue = PyObject_CallObject(pFunc, pArgs);
    Py_DECREF(pArgs);
    handle_python_error();

    if (!pValue) {
      Py_DECREF(pFunc);
      Py_DECREF(pModule);
      throw std::runtime_error("Call to 'fibonacci' failed.");
    }

    // --- Retrieve the return value from Python ---
    if (PyLong_Check(pValue)) {
      long long result = PyLong_AsLongLong(pValue);
      std::cout << "The " << n << "th Fibonacci number is: " << result
                << std::endl;
    } else {
      std::cerr << "Python function did not return a long." << std::endl;
    }

  } catch (const std::exception &e) {
    std::cerr << "Error: " << e.what() << std::endl;
    Py_Finalize();
    return 1;
  }

  // Finalize the Python interpreter.
  Py_Finalize();

  std::cout << "Application finished." << std::endl;

  return 0;
}
