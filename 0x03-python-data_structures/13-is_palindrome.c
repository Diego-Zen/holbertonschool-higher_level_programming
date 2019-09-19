#include "lists.h"
/**
 * is_palindrome - checks if a singly linked list is a palindrome
 *
 * @head: pointer head list
 *
 * Return: 0 if is not a palindrome or 1 if it is
 */
int is_palindrome(listint_t **head)
{
	listint_t *tmp1 = *head;
	listint_t *tmp2 = *head;

	int i = 0;
	int j = 0;
	int x = 0;
	int length = 0;

	if (*head == NULL)
		return (1);

	while (tmp2->next != NULL)
	{
		tmp2 = tmp2->next;
		i++;
	}
	length = (i + 1) / 2;
	while (j < length)
	{
		x = 0;
		if (tmp1->n != tmp2->n)
			return (0);
		tmp2 = *head;
		tmp1 = tmp1->next;
		i--;
		while (x < i)
		{
			tmp2 = tmp2->next;
			x++;
		}
		j++;
	}
	return (1);
}
