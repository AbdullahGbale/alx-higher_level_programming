#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome - checks if a list is palindrome
 * @head: pointer to head of a linked list
 * Return: returns 1, if the list has 1 element or is empty
 */

int is_palindrome(listint_t **head)
{
	if (*head == NULL || (*head)->next == NULL)
	{
		return (1);
	}
	listint_t *slow = *head;
	listint_t *fast = *head;

	while (fast->next != NULL && fast->next->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;
	}
	listint_t *prev = NULL;
	listint_t *current = slow->next;
	listint_t *next_node;

	while (current != NULL)
	{
		next_node = current->next;
		current->next = prev;
		prev = current;
		current = next_node;
	}
	listint_t *second_half = prev;
	listint_t *first_half = *head;

	while (second_half != NULL)
	{
		if (first_half->n != second_half->n)
		{
			return (0);
		}
		first_half = first_half->next;
		second_half = second_half->next;
	}

	return (1);
}
