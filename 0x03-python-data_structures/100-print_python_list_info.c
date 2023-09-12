#define PY_SSIZE_T_CLEAN
#include <stdio.h>
#include <Python.h>
#include <listobject.h>
#include <object.h>

/**
 * print_python_list_info - function
 * @p: PyObject
*/

void print_python_list_info(PyObject *p)
{
	long int size = Py_SIZE(p), i;
	PyListObject *item = (PyListObject *)p;

	size = PyList_Size(p);

	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", item->allocated);

	i = 0;

	while (i < size)
	{
		// item = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, Py_TYPE(PyList_GetItem(p, i))->tp_name);
		i++;
	}
}
