#Author: Andrew Apollo

import arrays 

def split(an_array):
    evens_count = (len(an_array) + 1 ) // 2 
    odds_count = len(an_array) // 2
    evens = arrays.Array(evens_count)
    odds = arrays.Array(odds_count)
    isEven = True

    for i in range (len(an_array)):
        if isEven:
            evens [i // 2] = an_array[i]
        else:
            odds [i // 2] = an_array[i]
        isEven = not isEven

    return(evens, odds)

def merge_sort(an_array):
    if len(an_array) == 0:
        return an_array
    elif len(an_array) == 1:
        return an_array
    else:
        (half1, half2) = split(an_array)
        return merge (merge_sort (half1) , merge_sort(half2))

def merge (sorted1 , sorted2 ):
    result = arrays.Array(len(sorted1) + len(sorted2))
    l1 = 0
    l2 = 0
    while l1 < len(sorted1) and l2 < len(sorted2):
        if sorted1 [l1] <= sorted2[l2]:
            result[l1 + l2] = sorted1[l1]
            l1 = l1 + 1
        else:
            result[l1 + l2] = sorted2[l2]
            l2 = l2 + 1

        if l1 < len(sorted1):
            for i in range (l1, len(sorted1)):
                result [i +l2] = sorted1[i]
        elif l2 < len(sorted2):
            for i in range (l2, len(sorted2)):
                result [i +l1] = sorted2[i]

        return result

def main(): 
    an_array = arrays.Array(5)
    an_array[0] = 10
    an_array[1] = 4
    an_array[2] = 6
    an_array[3] = 2
    an_array[4] = 8
    print(an_array)
    print(split(an_array))
    
    result =merge_sort(an_array)
    print(result)

main()
