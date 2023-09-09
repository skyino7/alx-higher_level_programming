#include "lists.h"

/**
 * check_cycle - checks to find a cycle in the linked linked
 * @list: list
 * Return: 1 for failure or 0 for success
*/

int check_cycle(listint_t *list)
{
	listint_t *slow;
	listint_t *fast;

	slow = list;
	fast = list;

	while (slow != NULL && fast != NULL && fast->next != NULL)
	{

		slow = slow->next;
		fast = fast->next->next;

		if (slow == fast)
			return (1);

	}

	return (0);
}
