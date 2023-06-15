'''
This is the logic for a calculator application

Includes methods for addition, subtraction, multiplication and division
Uses tkinter library/module for the GUI

Started : 18/05/2023
Author  : Matthew Tweedy
'''

def add(x, y):
    return round(x + y, 3)

def sub(x, y):
    return round(x - y, 3)

def multiply(x, y):
    return round(x * y, 3)

def divide(x, y):
    try:
        return round(x / y, 3)
    except ZeroDivisionError:
        return 0

def test():
    x = 20
    y = 5
    print(f"x = {x}\ny = {y}")
    print(f"adding {x} and {y} :", add(x,y))
    print(f"subtracting {x} and {y} :", sub(x,y))
    print(f"multiplying {x} and {y} :", multiply(x,y))
    print(f"dividing {x} and {y} :", int(divide(x,y)))

if __name__ =="__main__": test()