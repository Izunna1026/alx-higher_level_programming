#include "lists.h"
#include <stdlib.h>
#include <stddef.h>
/**
 * insert_node -to add a numbert in singly linked
 * @head:the variable
 * @number: this is the number to add
 * Return: to return NULL
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = *head, *first;

	first = malloc(sizeof(listint_t));
	if (first == NULL)
		return (NULL);
	first->n = number;

	if (node == NULL || node->n >= number)
	{
		first->next = node;
		*head = first;
		return (first);
	}

	while (node && node->next && node->next->n < number)
		node = node->next;

	first->next = node->next;
	node->next = first;

	return (first);
}
