#include <Python.h>
#include <stdio.h>

void print_python_string(PyObject *p) {
    PyUnicodeObject *unicode_obj;

    if (!PyUnicode_Check(p)) {
        printf("[.] string object info\n");
        printf("  [ERROR] Invalid String Object\n");
        return;
    }

    unicode_obj = (PyUnicodeObject *)p;
    printf("[.] string object info\n");
    printf("  type: %s\n", unicode_obj->compact ? "compact unicode object" : "compact ascii");
    printf("  length: %ld\n", PyUnicode_GET_LENGTH(p));
    printf("  value: %ls\n", PyUnicode_AsWideCharString(p, NULL));
}
