#Author: Andrew Apollo 

import arrays

#Class Activity 12.2.4
class Queue: 
    __slots__ = ["__front", "__back", "__size", "__array"]

    def __init__(self, capasity = 3):
        self.__array = arrays.Array(capasity)
        self.__front = 0 
        self.__back = 0 
        self.__size = 0 

    def is_empty(self):
        return self.__size == 0 

    def size(self):
        return self.__size

    #Class Activities 12.2.5 
    def __repr__(self):
        string = ''
        i = self.__front
        while i != self.__back:
            string += str(self.__array[i]) + ","
            i = (i + 1) % len(self.__array)

        return "[" + string[:2] + "]"

    #Class Activities 12.2.6
    def enqueue(self, value):
        self.__array[self.__back] = value
        self.__back = (self.__back + 1) % len(self.__array)
        self.__size += 1
        if self.__back == self.__front:
           self.__resize()

    #Class activity 12.2.7
    def get_front(self):
        return self.__front

    def get_back(self):
        return self.__back
    
    #Class activity 12.2.8
    def dequeue(self):
        if self.__size <= 0:
            raise IndexError ("Cannot dequeue from an empty queue")

        value = self.__array[self.__front]
        self.__front = (self.__front + 1) % len(self.__array)
        self.__size -= 1

        return value

    #Class activity 12.2.9
    def __resize(self):
        new_array = arrays.Array(len(self.__array)* 2 + 1)
        i = self.__front
        j = 0
        for _ in range(self.__size):
            new_array[j] = self.__array[i]
            i = (i + 1) % len(self.__array)
            j += 1

        self.__front = 0
        self.__back = j
        self.__array = new_array

def main():

    new_q = Queue(3)
    print(new_q)
    new_q.enqueue(5)
    new_q.enqueue(7)
    print(new_q)
    print(new_q.get_back)
    print(new_q.get_front)
    new_q.dequeue()
    print(new_q)
    new_q.dequeue()
    print(new_q)
    #new_q.dequeue()

    new_q.enqueue(6)
    new_q.enqueue(9)
    new_q.enqueue(6)
    new_q.enqueue(9)
    new_q.enqueue(6)
    new_q.enqueue(9)
    print(new_q)


main()