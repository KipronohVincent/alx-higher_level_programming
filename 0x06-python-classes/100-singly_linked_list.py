#!/usr/bin/python3
""" creating class Node """


class Node:
    """
    Defining a class node
    """

    def __init__(self, data=None, next_node=None):
        """Initializes the node."""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Returns the data of the node."""
        return self.__data

    @data.setter
    def data(self, value):
        """Sets the data to a value."""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Returns the next node."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Sets the next node to a value."""
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """
    Defining a class singly linked list
    """

    def __init__(self):
        """Initializes the data."""
        self.__head = None

    def __str__(self):
        """Returns a string representation of the list."""
        new_str = ""
        current_node = self.__head
        while current_node:
            new_str += str(current_node.data)
            current_node += '\n'
            current_node = current_node.next_node
        return new_str[:-1]

    def sorted_insert(self, value):
        """Inserts a new node at the correct position."""
        if self.__head is None:
            self.__head = Node(value)
            return
        current_node = self.__head
        previous_node = None
        while current_node is not None and current_node.data < value:
            previous_node = current_node
            current_node = current_node.next_node
        if previous_node is None:
            self.__head = Node(value, current_node)
        else:
            previous_node.next_node = Node(value, current_node)
