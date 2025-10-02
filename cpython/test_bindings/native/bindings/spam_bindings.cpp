#include <Python.h>
#include "spam.h"

static PyObject *SpamError;

// Python wrapper for spam::add
static PyObject *
spam_add(PyObject *self, PyObject *args)
{
    int a, b;
    
    if (!PyArg_ParseTuple(args, "ii", &a, &b))
        return NULL;
    
    int result = spam::add(a, b);
    return PyLong_FromLong(result);
}

// Python wrapper for spam::multiply
static PyObject *
spam_multiply(PyObject *self, PyObject *args)
{
    int a, b;
    
    if (!PyArg_ParseTuple(args, "ii", &a, &b))
        return NULL;
    
    int result = spam::multiply(a, b);
    return PyLong_FromLong(result);
}

// Python wrapper for spam::get_version
static PyObject *
spam_get_version(PyObject *self, PyObject *args)
{
    std::string version = spam::get_version();
    return PyUnicode_FromString(version.c_str());
}

// Python wrapper for spam::print_message
static PyObject *
spam_print_message(PyObject *self, PyObject *args)
{
    const char *message;
    
    if (!PyArg_ParseTuple(args, "s", &message))
        return NULL;
    
    spam::print_message(std::string(message));
    Py_RETURN_NONE;
}

const char spam_doc[] = "Native CPython bindings for the spam C++ library.";

static PyMethodDef SpamMethods[] = {
    {"add", spam_add, METH_VARARGS, "Add two integers."},
    {"multiply", spam_multiply, METH_VARARGS, "Multiply two integers."},
    {"get_version", spam_get_version, METH_NOARGS, "Get the library version."},
    {"print_message", spam_print_message, METH_VARARGS, "Print a message using the library."},
    {NULL, NULL, 0, NULL}        /* Sentinel */
};

static struct PyModuleDef spammodule = {
    PyModuleDef_HEAD_INIT,
    "spam",   /* name of module */
    spam_doc, /* module documentation, may be NULL */
    -1,       /* size of per-interpreter state of the module,
                 or -1 if the module keeps state in global variables. */
    SpamMethods
};

PyMODINIT_FUNC
PyInit_spam(void)
{
    PyObject *m;

    m = PyModule_Create(&spammodule);
    if (m == NULL)
        return NULL;

    SpamError = PyErr_NewException("spam.error", NULL, NULL);
    Py_INCREF(SpamError);
    PyModule_AddObject(m, "error", SpamError);
    return m;
}


