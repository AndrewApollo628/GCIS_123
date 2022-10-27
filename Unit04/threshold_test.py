'''
Author: Andrew Apollo

this program will test the distacne between 2 points to see if they are positive or negitive 
'''

def within_threshold(a, b , threshold):
     
    if a - b >= 0: # sees if the threshold is positive 
        return "True"
    elif a - b <= 0: # sees if the threshold is negitive 
        return "none"
    else:
        return "False"

    if a - b <= 0: # sees if the threshold is negitive 
        return "none"
'''
def test_threshold_positive():  #tests to see if the treshold is positive 
    out = within_threshold( 2 , 2 , 2)
    assert(out == "true")
'''

def test_threshold_negitive():#tests to see if the treshold is negitive
    neg = within_threshold(2, 3 , 1)
    assert(neg == "none")