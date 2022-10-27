#Author: Andrew Apollo

#Class activity 10.1.7 updated in 10.2.5
class Fruit:
    __slots__ = ["type","price","count"]
    def __init__(self, type, price):
        self.type = type
        self.price = price 
        self.count = 0

FRUITS = { "apple" :Fruit("Apple", 1.25),
           "pear"  :Fruit("Pear" , 1.35),
           "grapes":Fruit("Grapes" , 2.95)
}

def add_to_basket(fruit , basket):
    fruit = fruit.lower()
    if fruit in FRUITS:
        basket += [FRUITS[fruit]]
    elif fruit == '':
        pass
    else:
        print("Sorry we dont sell ", fruit, 's', sep="")

#Class activity 10.1.9
def calculate_cost(basket):
    cost = 0
    for fruit in basket:
        cost += fruit.price
        fruit.count += 1
    return cost

def main():
    #Class activity 10.1.7
    basket = []
    selection = None
    while selection != '':
        selection = input("WHich fruit would you like: ")
        add_to_basket (selection.lower(), basket)

    #Class activty 10.1.9
    cost = calculate_cost(basket)
    print("Thank you for purchasing:" , FRUITS['apple'].count , "Apples," , FRUITS['pear'].count , "Pears," , "and" , FRUITS['grapes'].count , "Grapes.")
    print("That comes to $" , round(cost, 3))

main()
