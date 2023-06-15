'''
CLI User Interface for calculator
'''

import calc_logic

menu = [
    "add",
    "subtract",
    "multiply",
    "divide",
    "QUIT"
]

def getMenuChoice(aMenu):
    '''getMenuChoice(aMenu) -> int
    
    takes a list of strings as input, displays as an
    enumerated list and loops until user selects a valid number
    '''

    if not aMenu : raise ValueError("no menu content")
    while True:
        for index, item in enumerate(aMenu, start=1):
            print(index, "\t", item)
        try:
            choice = int(input("choose an option : "))
            if 1 <= choice <= len(aMenu):
                return choice
            else:
                print("choose a number between 1 and", len(aMenu))
        except ValueError:
            print("choose the number of a menu option")
    
def executeChoice(choice):
    '''executeChoice(int) -> None
    
    execute whichever option the user selected.
    '''

    dispatch = [a, sub, multiply, divide, quit]
    calc = dispatch[choice-1]()
    if calc:
        # figure out how im gonna run the calculation
        print(f"---------------------\n\tresult\n\t{calc[0]} {calc[2]} {calc[1]} = {round(calc[3], 2)}\n---------------------")

def validateXY(operator):
    print(f"---------------------\n\tx {operator} y\n---------------------")
    while True:
        try:
            x = int(input("x : "))
        except ValueError:
            print("enter valid number")
            continue
        else:
            break
    while True:
        try:
            y = int(input("y : "))
        except ValueError:
            print("enter a valid number")
            continue
        else:
            break

    return list([x,y])

def a():
    op = "+"
    result = validateXY(op)
    x = result[0]
    y = result[1]
    return list([x ,y, op, calc_logic.add(x,y)])

def sub():
    op = "-"
    result = validateXY(op)
    x = result[0]
    y = result[1]
    return list([x, y, op, calc_logic.sub(x,y)])

def multiply():
    op = "*"
    result = validateXY(op)
    x = result[0]
    y = result[1]
    return list([x, y, op, calc_logic.multiply(x,y)])

def divide():
    op = "/"
    result = validateXY(op)
    x = result[0]
    y = result[1]
    return list([x, y, op, calc_logic.divide(x,y)])

def quit():
    print("---------------------\n\texiting\n---------------------")
    raise SystemExit

def main():
    while True:
        choice = getMenuChoice(menu)
        executeChoice(choice)

if __name__ == "__main__": main()
