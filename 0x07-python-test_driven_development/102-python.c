#include <Python.h>

/**
 * print_python_string - Prints Python string information.
 * @p: PyObject string pointer.
 */
void print_python_string(PyObject *p)
{
    printf("[.] string object info\n");

    if (PyUnicode_Check(p))
    {
        if (PyUnicode_IS_COMPACT_ASCII(p))
            printf("  type: compact ascii\n");
        else
            printf("  type: compact unicode object\n");

        printf("  length: %ld\n", PyUnicode_GET_LENGTH(p));
        printf("  value: %ls\n", PyUnicode_AsWideCharString(p, NULL));
    }
    else
    {
        printf("  [ERROR] Invalid String Object\n");
    }
}
