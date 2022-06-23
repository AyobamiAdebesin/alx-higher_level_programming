#!/usr/bin/python3
""" A class that defines a node of a singly linked list
    and a Singly Linked List
"""


class Node:
    """
    A class that defines a node of a singly linked list
    """
    def __init__(self, data, next_node=None):
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        return  self.__data

    @data.setter
    def data(self, value):
        if type(value) != int:
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if isinstance(value, Node) and value is not None:
            raise TypeError("next_node mus be a Node object")
        else:
            self.__next_node = value

class SinglyLinkedList:
    """
    A class that defines a singly linked list
    
    """

    def __init__(self):
        self.__head = None


    def __str__(self):
        rtn = ""
        ptr = self.__head

        while ptr is not None:
            rtn += str(ptr.data)
            if ptr.next_node is not None:
                rtn += "\n"
            ptr = ptr.next_node

        return rtn


    def sorted_insert(self, value):
        ptr = self.__head

        while ptr is not None:
            if ptr.data > value:
                break
            ptr_prev = ptr
            ptr = ptr.next_node

        newNode = Node(value, ptr)
        if ptr == self.__head:
            self.__head = newNode
        else:
            ptr_prev.next_node = newNode
