#include "lists.h"
#include <stdlib.h>

/**
 * insert_node - Inserts a node into a sorted singly linked list
 *
 * @head: A pointer to a pointer to the first node of the list
 * @number: The number to be inserted into the list
 *
 * Return: The address of the new node or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
    listint_t *new_node, *current_node;

    if (!head)
        return (NULL);

    new_node = malloc(sizeof(listint_t));
    if (!new_node)
        return (NULL);

    new_node->n = number;

    if (*head == NULL || (*head)->n >= number)
    {
        new_node->next = *head;
        *head = new_node;
        return (new_node);
    }

    current_node = *head;

    while (current_node->next != NULL && current_node->next->n < number)
        current_node = current_node->next;

    new_node->next = current_node->next;
    current_node->next = new_node;

    return (new_node);
}
