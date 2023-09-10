#include "lists.h"

/**
 * is_palindrome - function
 * @head: node
 * Return: 1 0r 0
*/

int is_palindrome(listint_t **head)
{
    listint_t *slow;
    listint_t *fast;

    slow = head;
    fast = head;

    if (head == NULL && *head == NULL)
        return (NULL);

    while (slow != NULL && fast != NULL)
    {
        fast = fast->next->next;
        slow = slow->next;
    }

}