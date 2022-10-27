'''
Author: Andrew Apollo 

This program will 
    - unload a shipment of droids
'''

def unload_shipment(filename, belt = []):
    '''
    This function will
        - look at a file and unload the parts 
        - return the parts 
    Paramaters
        - filename: file in which the parts are being read from
        - belt: list of parts that are in the file
    '''
    with open(filename) as file:
        for part in file:
            belt.append(part)
        
        return belt


def main():

    #HW activity 5 main test 
    file = ("droid_parts/parts_0001_0001.txt")
    print(unload_shipment(file))

main()