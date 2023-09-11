#define PY_SSIZE_T_CLEAN
#include <stdio.h>
#include <Python.h>

/**
 * print_python_list_info - function
 * @p: PyObject
*/

void print_python_list_info(PyObject *p)
{
	Py_ssize_t size, i;
	PyObject *item;

	size = PyList_Size(p);

	printf("[*] Size of the Python List = %zd\n", size);
	printf("[*] Allocated = %zd\n", ((PyListObject *)p)->allocated);

	i = 0;

	while (i < size)
	{
		item = PyList_GetItem(p, i);
		printf("Element %zd: %s\n", i, Py_TYPE(item)->tp_name);
		i++;
	}
}
