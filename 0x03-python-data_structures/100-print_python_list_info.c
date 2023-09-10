#include <stdio.h>
#include <python.h>
#include <object.h>
#include <listobject.h>

/**
 * print_python_list_info - function
 * @p: PyOject
*/

void print_python_list_info(PyObject *p)
{
    int i;
    PyListObject *pp

    pp = (PyListObject *)p;

    printf("[*] Size of the Python List = %ld\n", pp->ob_base.ob_size);
    printf("[*] Allocated = %ld\n", pp->allocated);

    i = 0;

    while (i < ob_base.ob_size)
    {
        printf("Element %d: %s\n", i, pp->ob_item[i]->ob_type->tp_name);
        i++;
    }

}
