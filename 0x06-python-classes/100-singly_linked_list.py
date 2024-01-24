#!/usr/bin/python3
"""Defines a singly linked list."""


class Node:
    """A node of a singly linked list."""
    def __init__(self, data, next_node=None):
        """Initialize a node with data and optional next_node."""
        self.data = data
        self.next_node = next_node


class SinglyLinkedList:
    """A singly linked list."""
    def __init__(self):
        """Initialize an empty singly linked list."""
        self.head = None

    def sorted_insert(self, value):
        """Insert a new Node into the sorted position."""
        new_node = Node(value)
        if not self.head or self.head.data > value:
            new_node.next_node = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next_node and current.next_node.data < value:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node

    def __str__(self):
        """Return a string representation of the linked list."""
        result = ""
        current = self.head
        while current:
            result += str(current.data) + "\n"
            current = current.next_node
        return result.rstrip()
