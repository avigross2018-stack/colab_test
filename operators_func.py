# This function adds two numbers together
def multi(num_1,num_2):
    return num_1 * num_2


# This function divides two numbers
def divide(num_1,num_2):
    try:
        result = num_1 / num_2
        return result
    except ZeroDivisionError:
        return "Error: You cannot divide by zero! 😅"


# This function adds two numbers together
def add(num_1,num_2):
    return num_1 + num_2


def sub(a,b):
    '''
    Docstring for sub
    subtract a and b
    
    :param a: number
    :param b: number
    '''
    return a - b

def power(a,b):
    '''
    Docstring for power
    a in power of b
    :param a: number
    :param b: number
    '''
    return a ** b

def root(a):
    '''
    Docstring for root
    a in power of (0.5)
    :param a: int number
    '''
    return a ** 0.5

# This function return the absolute value
def absolute_value(number):
    if number < 0:
        return - number
    else:
        return number
    
    
# This function returns the area of ​​a triangle
def triangle_area(num_1,num_2):
    return num_1 * num_2 / 2


# This function returns the area of ​​a square
def square_area(number):
    return number ** 2


# This function returns the area of ​​a rectangle
def rectangle_area(num_1,num_2):
    return num_1 * num_2


# This function returns the area of ​​a circle
import math

def circle_area(radius):
    if radius < 0:
        return "radius cannot be negative!"
    
    return math.pi * (radius ** 2)

