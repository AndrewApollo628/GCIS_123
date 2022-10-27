#Author: Andrew Apollo

import random 
import array_queue
import node_stack
STORE = {}

'''
Activity 13.3.2
Data type:      Complexity Access:  Complexity Insert:  is orderable:  value must be unique:

Array           O(c)                O(N)                Y              N

List            O(c)                O(N)                Y              N

Dictonary       O(C)                O(C)                N              Keys

Set             O(C)                O(C)                N              Y

Stack           O(C)                O(C)                ordered        N

Queue           O(C)                O(C)                ordered        N
'''

#Activity 13.3.3
class GroceryItem:
    __slots__ = ["__name","__weight", "__price" ]

    def __init__(self, name, weight, price):
        self.__name = name
        self.__weight = weight
        self.__price = price

    def get_name(self):
        return self.__name

    def get_weight(self):
        return self.__weight

    def get_price(self):
        return self.__price

    #Activity 13.3.4
    def __repr__(self):
        return self.__name + " " + str(self.__weight) + "lb $" + str(self.__price)

    def __hash__(self):
        return hash(self.__name)

    def __eq__(self,other):
        if type(self) == type(other):
            return self.__name == other.__name
        else:
            return False

    def __lt__ (self, other):
        if type(self) == type(other):
            return self.__weight < other.__weight
        else:
            raise TypeError("'<' not supported between instances of ") \
                + type(self).__name__ + "and" \
                + type(other).__name__

#Activity 13.3.6
class Customer:
    __slots__ = ["__list", "__cart", "__bags"]

    def __init__(self, item_names, list_size = 25):
        self.__list = []
        self.__cart = set()
        self.__bags = []

        #Activity 13.3.7
        random.shuffle(item_names)
        for i in range(list_size):
            self.__list += [item_names[i]]

    def get_bags(self):
        return self.__bags

    #Activity 13.3.7
    def get_list(self):
        return self.__list

    #Activity 13.3.8
    def shop(self, store):
        for grocery in self.__list:
            self.__cart.add(store[grocery])
    
    def get_cart(self):
        return self.__cart

    #Activity 13.3.9
    def unload(self):
        belt = array_queue.Queue()
        for item in self.__cart:
            belt.enqueue(item)
        return belt

    #Activity 13.3.12
    def unpack(self):
        for bag in self.__bags:
            print("New bag:")
            while not bag.is_empty():
                print(bag.pop())

def make_item(item_number):
    name = "Item #" + str(item_number)
    weigth = random.randint(1,10)
    price = random.randint(1,20)
    return GroceryItem(name, weigth, price)

#Activity 13.3.5
def fill_store(store, num_items):
    for i in range(num_items):
        item = make_item(i)
        store[item.get_name()] = item

#Activity 13.3.10
'''
1) If new item is less weight than old item add it 
2) if item is hevier than the previous add a bag
3) stack
'''

#Activity 13.3.11
def cashier(belt, customer):
    total_bill = 0 
    while not belt.is_empty():
        item = belt.dequeue()
        total_bill += item.get_price()
        bagged = False
        for bag in customer.get_bags():
            if bag.peek().get_weigth() > item.get_weight():
                bag.push(item)
                bagged = True
                break
            if not bagged:
                bag = node_stack.Stack()
                bag.push(item)
                customer.get_bags().append(bag)
    return total_bill


def main():

    #Activity 13.3.3
    '''
    new_item = make_item(10)
    print(new_item)

    #Activity 13.3.4
    items = []
    for i in range(5):
        items.append(make_item(i))
    items.sort()
    print(items)
    '''
    #Activity 13.3.5
    fill_store(STORE, 100)
    
    #Activity 13.3.7
    item_names = list(STORE.keys())
    bruce = Customer(item_names)
    #Activity 13.3.8
    bruce.shop(STORE)
    #Activity 13.3.9
    belt = bruce.unload()
    cost = cashier(belt, bruce)
    
    bruce.unpack()

main()