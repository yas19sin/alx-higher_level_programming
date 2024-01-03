#ifndef LISTS_H
#define LISTS_H

#include <stdio.h>
#include <stdlib.h>
#include <stddef.h>
/**
 * struct listint_s - A node in a singly linked list of integers
 * @n: The integer data stored in the node
 * @next: A pointer to the next node in the list
 *
 * Description: Defines a node structure for a singly linked list
 */

typedef struct listint_s
{
	int n;
	struct listint_s *next;
} listint_t;

size_t print_listint(const listint_t *h);
listint_t *add_nodeint_end(listint_t **head, const int n);
void free_listint(listint_t *head);

listint_t *insert_node(listint_t **head, int number);

#endif /* LISTS_H */