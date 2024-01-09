#include <Python.h>
#include <stdio.h>

/**
 * print_python_list_info - prints basic info about Python lists
 * @p: PyObject pointer to the Python list
 */
void print_python_list_info(PyObject *p)
{
    PyListObject *list = (PyListObject *)p;
    unsigned int size, idx;
    PyTypeObject *type;

    if (p == NULL || !PyList_Check(p))
        return;

    size = Py_SIZE(p);
    printf("[*] Size of the Python List = %u\n", size);
    printf("[*] Allocated = %u\n", (unsigned int)list->allocated);

    for (idx = 0; idx < size; idx++)
    {
        type = Py_TYPE(list->ob_item[idx]);
        printf("Element %u: %s\n", idx, type->tp_name);
    }
}
