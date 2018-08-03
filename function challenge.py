#function that takes a string as input and returns the first character of the string

def string(first):
    while True:
        return first[0]

#takes in a list as input and returns the product of all numbers in that list

def list_(product):
    oo =1
    for num in product:
        oo *= num
    return oo
    
#takes string and returns that string with an exclamation mark added to the end

def excited(string):
    return string + ("!")

#takes list and returns true if the 1st element of list is equal to the last element

def num_list(element):
    while True:
        if element[0] == element[(len(element)-1)]:
            return True
        else:
            return False

#takes int and returns sum of all intergers from 0 to that int

def allints(sumint):
    total=0
    for ok in sumint:
        total += len(sumint)
    return total
