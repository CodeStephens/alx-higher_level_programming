#include "lists.h"

/**
 * reverse_listint - performs reversal operation on singly linked list
 * @head: pointer to the address of the reversed linked list starting node
 *
 * Description:
 * Return: a pointer to the starting node of the reversed linked list
 */
listint_t *reverse_listint(listint_t **head)
{
	listint_t *node = *head, *next, *prev = NULL;
	while (node)
	{
		next = node->next;
		node->next = prev;
		prev = node;
		node = next;
	}
	*head = prev;
        return (*head);
}

/**
 * is_palindrome - checks for palindrome in a singly linked list
 * @head: A pointer to the starting node of the singly linked list
 *
 * Description:
 * Return: 0 if the linked list is not a palindrome, and 1 if the linked
 * listint_t is a palindrome
 */
int is_palindrome(listint_t **head)
{
        listint_t *tmp, *rev, *mid;
        size_t size = 0, i;

        if (*head == NULL || (*head)->next == NULL)
                return (1);

        tmp = *head;
        while (tmp)
        {
                size++;
                tmp = tmp->next;
        }

        tmp = *head;
        for (i = 0; i < (size / 2) - 1; i++)
                tmp = tmp->next;

        if ((size % 2) == 0 && tmp->n != tmp->next->n)
                return (0);

        tmp = tmp->next->next;
        rev = reverse_listint(&tmp);
        mid = rev;

        tmp = *head;
        while (rev)
        {
                if (tmp->n != rev->n)
                        return (0);
                tmp = tmp->next;
                rev = rev->next;
        }
        reverse_listint(&mid);

        return (1);
}
