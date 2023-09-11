#include "lists.h"

listint_t *reverse(listint_t *head)
{
    listint_t *prev = NULL;
    listint_t *current = head;
    listint_t *next;

    while (current != NULL)
    {
        next = current->next;
        current->next = prev;
        prev = current;
        current = next;
    }

    return (prev);
}

/**
 * is_palindrome - function
 * @head: node
 * Return: 1 0r 0
*/

int is_palindrome(listint_t **head)
{
    listint_t *fast = *head;
    listint_t *slow = *head;
    listint_t *second;
    listint_t *middle = NULL;
    int isPalindrome = 1;

    if (*head == NULL || (*head)->next == NULL)
        return (1);

    while (fast != NULL && fast->next != NULL)
    {
        fast = fast->next->next;
        slow = slow->next;
    }

    if (fast != NULL)
    {
        middle = slow;
        slow = slow->next;
    }

    second = reverse(slow);

    while (second != NULL)
    {
        if ((*head)->n != second->n)
        {
            isPalindrome = 0;
            break;
        }

        *head = (*head)->next;
        second = second->next;

    }

    if (middle != NULL)
        middle->next = reverse(middle->next);

    return (isPalindrome);

}