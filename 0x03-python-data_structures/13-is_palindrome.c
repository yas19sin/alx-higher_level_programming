#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to the head of the linked list
 *
 * Return: 1 if it is a palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
    listint_t *slow = *head, *fast = *head, *prev = NULL;
    listint_t *second_half, *mid_node;
    int is_palindrome = 1;

    if (*head == NULL || (*head)->next == NULL)
        return (1);

    while (fast && fast->next)
    {
        fast = fast->next->next;
        mid_node = slow;
        slow = slow->next;
    }

    if (fast)
        mid_node = slow;

    second_half = reverse_list(&slow);
    prev = *head;

    while (second_half)
    {
        if (second_half->n != prev->n)
        {
            is_palindrome = 0;
            break;
        }
        second_half = second_half->next;
        prev = prev->next;
    }

    reverse_list(&slow);

    if (mid_node)
        mid_node->next = slow;

    return is_palindrome;
}

/**
 * reverse_list - reverses a linked list
 * @head: pointer to the head of the linked list
 *
 * Return: pointer to the new head of the reversed list
 */
listint_t *reverse_list(listint_t **head)
{
    listint_t *prev = NULL, *current = *head, *next;

    while (current)
    {
        next = current->next;
        current->next = prev;
        prev = current;
        current = next;
    }

    *head = prev;
    return *head;
}
