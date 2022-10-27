#Author: Andrew Apollo 

import node

class Stack:

    #Class activity 12.1.5
    __slots__ = ["__size", "__top"]

    def __init__(self):
        self.__size = 0
        self.__top = None

    def size(self):
        return self.__size

    def is_empty(self):
        return self.__top == None

    #Class activity 12.1.6
    def __stringify (self, node):
        if node == None:
            return " "
        else:
            return self.__stringify(node.get_next()) + str(node.get_value()) + ", "

    def __repr__(self):
        string = self.__stringify(self.__top)
        return "[" + string[:-2] + "]" 

    #Class activity 12.1.7
    def push(self, value):
        new_node = node.Node(value, self.__top)
        self.__top = new_node
        self.__size += 1

    #Class activity 12.1.8
    def peak(self):
        return self.__top.get_value()

    #Class activity 12.1.9
    def pop(self):
        value = self.__top.get_value()
        self.__top = self.__top.get_next()
        self.__size -= 1
        return value
