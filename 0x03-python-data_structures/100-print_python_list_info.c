#include <stdio.h>
#include <python.h>
<<<<<<< HEAD
#include <object.h>
#include <listobject.h>
=======
>>>>>>> 72e94a071cd397d97e3878312c31e52a963df49f

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
<<<<<<< HEAD
	i++;
=======
        i++;
>>>>>>> 72e94a071cd397d97e3878312c31e52a963df49f
    }

}
