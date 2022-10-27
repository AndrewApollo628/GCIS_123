''' 
Author: Andrew Apollo

This program will
    - Store pizza toppings
    - Store a pizza 
    - Allow customers to buy a pizza 
'''

from os import sep


class toppings():
    '''
    This class will 
        - initalize the toppings atributes 
    '''
    __slots__ = ["code", "topping" , "price"]

    def __init__(self , code, topping, price):
        '''
        This function will
            - initalize the toppings atributes 
        '''
        self.topping = topping
        self.code = code 
        self.price = price

class pizza():
    '''
    This class will 
        - initilize pizza atributes 
    '''
    __slots__ = ["price" , "veggies" , "meats" , "cheese"]

    def __init__(self):
        '''
        This function will 
            - initilize pizza atributes 
        '''
        self.price = 5.0
        self.veggies = set()
        self.meats = set()
        self.cheese = set() 

#Cheese Options 
_CHEESES = {"a": toppings("a", "Added Cheese", 1.5),
            "f": toppings("f", "Fresh Mozzerella", 2.0),
            "r": toppings("r", "Ricotta", 1.5)
           }

#Meat Options 
_MEATS = {"p": toppings("p" , "Pepperoni", .5),
          "h": toppings("h", "Ham", .5),
          "s": toppings("s", "Sausage", .5)
         }

#Veggie Options
_VEGGIES = {"m": toppings("m", "Mushrooms", .5),
            "p": toppings("p", "Peppers", .5),
            "t": toppings("t", "Tomato", .5)
           }
        
def print_cheese_options():
    '''
    This function will
        - Print out the cheese options for the pizza 
    '''
    print("Cheese Options:")
    print(_CHEESES['a'].topping, "(", _CHEESES['a'].code , ") " , ": $" , _CHEESES['a'].price , "  ",  
          _CHEESES['f'].topping, "(", _CHEESES['f'].code, ") " , ": $" , _CHEESES['f'].price , "  ",
          _CHEESES['r'].topping, "(", _CHEESES['r'].code, ") " ,": $" , _CHEESES['r'].price , "  ", sep=""
            )

def print_meat_options():
    '''
    This function will
        - Print out the meat options for the pizza 
    '''
    print("Meat Options:")
    print(_MEATS['p'].topping, "(", _MEATS['p'].code , ") " , ": $" , _MEATS['p'].price , "  ",  
          _MEATS['h'].topping, "(", _MEATS['h'].code, ") " , ": $" , _MEATS['h'].price , "  ",
          _MEATS['s'].topping, "(", _MEATS['s'].code, ") " ,": $" , _MEATS['s'].price , "  ", sep=""
            )

def print_veggie_options():
    '''
    This function will
        - Print out the veggie options for the pizza 
    '''
    print("Meat Options:")
    print(_VEGGIES['m'].topping, "(", _VEGGIES['m'].code , ") " , ": $" , _VEGGIES['m'].price , "  ",  
          _VEGGIES['p'].topping, "(", _VEGGIES['p'].code, ") " , ": $" , _VEGGIES['p'].price , "  ",
          _VEGGIES['t'].topping, "(", _VEGGIES['t'].code, ") " ,": $" , _VEGGIES['t'].price , "  ", sep=""
            )

def order_pizza():
    '''
    This function will
        - Prompt the user for the catagories of a pizza order
        - return the pizza order made by the user 
    '''
    pizza_order = []

    #Asking user for cheese option
    ch_option = input("Enter the cheese option of your choice, for options enter (o): ")
    
    if ch_option == 'o':
        print_cheese_options()
        ch_option = input("Enter the cheese option of your choice: for options enter (o) ")
    

    for cheese in ch_option:
        if cheese in _CHEESES:
            pizza_order.append(cheese)

    #Asking the user for meat options
    meat_option = input("Enter the meat option of your choice, for options enter (o): ")
    if meat_option == 'o':
        print_meat_options()
        meat_option = input("Enter the meat option of your choice: for options enter (o) ")
        
    for meat in meat_option:
        if meat in _MEATS :
            pizza_order.append(meat)

    #Asking the user for Veggie options
    veg_option = input("Enter the veggie option of your choice, for options enter (o): ")
    if veg_option == 'o':
        print_veggie_options()
        veg_option = input("Enter the veggie option of your choice: for options enter (o) ")
        
    for veggie in veg_option:
        if veggie in _VEGGIES :
            pizza_order.append(veggie)

    return pizza_order

def add_toppings(pizza_order):
    '''
    This function will 
        - add toppings to the pizza 
        - returns all toppings on pizza 
    
    Paramaters
        - Pizza: Pizza being passed in
    '''
    cost = 5.0
    ch_names =[]
    meat_names = []
    veg_names = []

    #Getting toppings and added the names to the list of toppings category they are from 
    for topping in pizza_order:
        if topping in _CHEESES:
            ch_names.append(_CHEESES[topping].topping)
            cost += float(_CHEESES[topping].price)
        if topping in _MEATS:
            meat_names.append(_MEATS[topping].topping)
            cost += float(_MEATS[topping].price)
        if topping in _VEGGIES:
            veg_names.append(_VEGGIES[topping].topping)
            cost += float(_VEGGIES[topping].price)
    
    return ch_names , meat_names, veg_names , cost 

def print_pizza_order(cheese , meats , veggies):
    '''
    This function will 
        - print the pizza order 

    Paramaters
        - cheese: cheeses on pizza 
        - meats: meats on pizza 
        - veggies: veggies on pizza 
    ''' 
    print("One pizza with", end= ", ")
    for ch in cheese:
        print(ch , end = ", ")
    for meat in meats:
        print(meat, end = ", ")
    for veggie in veggies:
        print(veggie)

    
def main():

    print("Welcome to Apollo's Pizza Palace") 
    print("Your First Pizza Order: ")
    cheese, meat, veg, cost1 = add_toppings(order_pizza())
    print_pizza_order(cheese, meat, veg)
    print("Your Second Pizza Order: ")
    cheese2, meat2, veg2, cost2  = add_toppings(order_pizza())
    print_pizza_order(cheese2, meat2, veg2)
    print("Total Due: $", cost1 + cost2, sep= "")

main()    