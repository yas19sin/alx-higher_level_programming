#define PY_SSIZE_T_CLEAN
#include <Python.h>

/**
 * print_python_bytes - Print information about Python bytes object
 * @p: PyObject
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t size, i;
	char *str;

	printf("[.] bytes object info\n");

	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	size = PyBytes_Size(p);
	str = PyBytes_AsString(p);

	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", str);

	printf("  first %ld bytes: ", size < 10 ? size + 1 : 10);
	for (i = 0; i <= size && i < 10; ++i)
		printf("%02x%c", (unsigned char)str[i], i == size || i == 9 ? '\n' : ' ');

	(void)p;
}


/**
 * print_python_list - Print information about Python list object
 * @p: PyObject
 */
void print_python_list(PyObject *p)
{
	PyListObject *list;
	Py_ssize_t size, i;
	
	printf("[*] Python list info\n");

	if (!PyList_Check(p))
	{
		printf("  [ERROR] Invalid List Object\n");
		return;
	}

	list = (PyListObject *)p;
	size = PyList_Size(p);

	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", list->allocated);

	for (i = 0; i < size; ++i)
	{
		PyObject *item = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
	}
}

/**
 * print_python_float - Print information about Python float object
 * @p: PyObject
 */
void print_python_float(PyObject *p)
{
	PyFloatObject *float_obj;

	printf("[.] float object info\n");

	if (!PyFloat_Check(p))
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}

	float_obj = (PyFloatObject *)p;
	printf("  value: %f\n", float_obj->ob_fval);
}
