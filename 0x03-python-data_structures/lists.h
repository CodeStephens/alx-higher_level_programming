#ifndef LIST_H
#define LIST_H

	#include <stdio.h>
	#include <stdlib.h>
	#include <CPython.h>
/**
 * struct listint_s - singly linked list
 * @n: integer
 * @next: pointer to the next address in the listint_s
 *
 * Description:
 */
	typedef struct listint_s
	{
        	int n;
        	struct listint_s *next;
	} listint_t;

	void print_python_list_infor(PyObject *p);
	size_t print_listint(const listint_t *h);
	listint_t *add_nodeint_end(listint_t **head, const int n);
	void free_listint(listint_t *head);
	int is_palindrome(listint_t **head);

#endif /* LIST_H */
