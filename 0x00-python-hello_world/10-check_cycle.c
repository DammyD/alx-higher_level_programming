#include "lists.h"

/**
 * check_cycle - checks if a singly linked has a cycle in it
 * @list: pointer to the list
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *new;
		listint_t *old;
	new = list;
	old = list;
	while (list && new && new->next)
	{
		list = list->next;
		new = new->next->next;

		if (list == new)
		{
			list = old;
			old = new;
			while (1)
			{
				new = old;
				while (new->next != list && new->next != old)
				{
					new = new->next;
				}
				if (new->next == list)
					break;

				list = list->next;
			}
			return (1);
		}
	}
	return (0);
}
