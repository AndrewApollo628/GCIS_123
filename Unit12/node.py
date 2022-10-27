#Author: Andrew Apollo 

class Node: 
    #Class activity 12.1.3
    __slots__ = ["__value", "__next"]

    def __init__(self, value, next =None):
        self.__value = value
        self.__next = next

    def get_value(self):
        return self.__value

    def get_next(self):
        return self.__next

    #Class activity 12.1.4
    def print_node(node_seq):
        if node_seq == None:
            return ''
        else:
            print(node_seq.get_value(), end= ", ")
            print(node_seq.get_next())