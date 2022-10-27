'''
Author: Andrew Apollo 

This program will plot graes based on a specific student 

'''

#Import statements 
import plotter 

def quit(): 
    '''
    This function will prompt the user to make surer they want to quit 
    if the input is Y or y the program will quit 
    '''

    user = input("Are you sure? (y/n): ")
    if user == "Y" or "y":
        print("Goodbye!")
        return True
    else:
        return False

def plot_grades(filename , firstname , lastname):
    '''
    This function will use plotter ro plot grades for a specified student

    Paramaters:
        filename: file where the data is coming from 
        firstname: first name of the specified student
        lastname: last name of the specified student
    '''
    
    fn = firstname
    ln = lastname
    fn = fn.lower()
    ln = ln.lower()
    with open(filename) as file:
        next(file)
        plotter.init(firstname , "Score" , "Grade Item")
        
        for line in file:
            file_word = line.split(",")
            
            if fn == file_word[1].lower() and ln == file_word[0].lower():
                for col in file_word:
                    try:
                        plotter.add_data_point(int(col))
                    except:
                        pass
        
        plotter.plot()
            

        

def student_grades(argument):
    '''
    This function will take in a sequence of string arguments 
    and will call plot grades and plot grades

    Paramaters:
        argument: is the user input from main broken up and set as the paramnaters
                  of plot_grades()
    
    '''
    filename = argument[1]
    firstname = argument[2]
    lastname = argument[3]

    plot_grades(filename ,firstname ,lastname)

def help():
    print("stu <filename> <firstname> <lastname> ")
    print("item")
    print(" quit - quits")
    print("help - displays this message")


def main(): 
    """
    This function will input user input and see if teh command is to quit 
    if the command = quit than the quit function will be called 
    if there is a blank input the error will be excepted and the input will be asked again
    """

    try:
      while True:
        user_in = input("Enter command: ")
        command = user_in.split()
        if command[0] == "quit":
            quit()
            break
        elif command[0] == "stu":
            student_grades(command)
        elif command[0] == "help":
            help()
        else:
            break
            
        
    except IndexError:
        print("Enter command or 'quit' to quit")
    except TypeError:
        print("Usage: stu <filename> <firstname> <lastname>")
    except FileNotFoundError:
        print("File not found " , command)
    
main()