#include "lists.h"
/**
 * check_cycle - to check the cycle
 * @list: the variable
 * Return: to return 0 if no cycle and 1 if there isa cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *s, *f;

	if (!list || !list->next)
		return (0);
	f = list;
	s = list;

	while (s != NULL && f != NULL && f->next != NULL)
	{
		s = s->next;
		f = f->next->next;
		if (s == f)
			return (1);
	}
	return (0);
}
