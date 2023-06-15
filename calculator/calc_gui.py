import tkinter as tk
import tkinter.messagebox as mb
import calc_logic


# TODO: STARTED THIS ONE
# add '.' for decimal points
# -------------------------- 
# TODO: 30/05/23
# add <- backspace for misinputs
# MAYBE: if user presses "-" allow it to change first number to negative
# get File and Help menu working

top = tk.Tk()
operators = ["<-", "+", "-", "x", "÷", "=", ".", "AC"]
calc = "0"
lastAnswer = ""

# parse "calc" string for operations
def parseCalcString():
    global calc

    # split the calculation string, save each argument and return
    splitCalcString = calc.split(' ')
    return splitCalcString

def checkCalcString():
    global calc
    global lastAnswer
    splitCalcString = parseCalcString()

    # if splitCalcString is greater than 1 but last arg is an operator, dont do anything
    if len(splitCalcString) > 1:
        # if last arg is an operator or blank, dont do anything
        if splitCalcString[-1] == "+" or splitCalcString[-1] == "-" or splitCalcString[-1] == "x" or splitCalcString[-1] == "÷" or splitCalcString[-1] == "":
            return 0
        lastAnswer = evCalculate()
        return 1
    else:
        return 1
    
def concatNumber(num):
    global calc
    global lastAnswer

    if calc == "0" or calc == str(lastAnswer):
        calc = str(num)
    else:
        calc = calc + str(num)

    return calc

# event handler functions
# add the correct operator to calc string
def evAdd():
    global calc
    if checkCalcString():
        calc = calc + " " + operators[1] + " "
    else:
        return

def evSub():
    global calc
    if checkCalcString():
        calc = calc + " " + operators[2] + " "
    else:
        return

def evMultiply():
    global calc
    if checkCalcString():
        calc = calc + " " + operators[3] + " "
    else:
        return

def evDivide():
    global calc
    if checkCalcString():
        calc = calc + " " + operators[4] + " "
    else:
        return

def evAC():
    global calc
    calc = "0"

# calc GUI logic for inputting numbers and the options:
    # calc default string = "0"
    # any number input will overwrite default
    # any operation pressed while default will take x as 0
    # if operation pressed when last char in calc string = operation:
    #       don't change calc string
    # parse calc string to get x, y, op (split on " ")
    #       and pass onto logic
    # pressing "=" button will then call correct logic function/method
def evCalculate():
    global calc
    splitCalcString = parseCalcString()
    
    if len(splitCalcString) < 2:
        return calc

    if splitCalcString[1] == "+" and splitCalcString[2] != '':
        # calc_logic.add(float(calc[0]), float(calc[2]))
        answer = calc_logic.add(float(splitCalcString[0]), float(splitCalcString[2]))
        if str(answer).split('.')[1] == "0":
            calc = str(int(answer))
        else:
            calc = str(answer)
        return answer
    elif splitCalcString[1] == "-" and splitCalcString[2] != '':
        # answer = calc_logic.sub(float(calc[0]), float(calc[2]))
        answer = calc_logic.sub(float(splitCalcString[0]), float(splitCalcString[2]))
        if str(answer).split('.')[1] == "0":
            calc = str(int(answer))
        else:
            calc = str(answer)
        return answer
    elif splitCalcString[1] == "x" and splitCalcString[2] != '':
        answer = calc_logic.multiply(float(splitCalcString[0]), float(splitCalcString[2]))
        if str(answer).split('.')[1] == "0":
            calc = str(int(answer))
        else:
            calc = str(answer)
        return answer
    elif splitCalcString[1] == "÷" and splitCalcString[2] != '':
        if splitCalcString[0] == "0" or splitCalcString[2] == "0":
            answer = "Cannot divide by zero!"
            calc = answer
            return answer
        answer = calc_logic.divide(float(splitCalcString[0]), float(splitCalcString[2]))
        print(str(answer))
        if str(answer).split('.')[1] == "0":
            calc = str(int(answer))
        else:
            calc = str(answer)
        return answer
    else:
        pass

def evHelp():
    mb.showinfo("Help", '''
    +  : add two numbers
    -  : subtract second number from first
    *  : multiply two numbers together
    /  : divide first number by second
    =  : calculate answer
    AC : clear calculator
    ''')

def evAbout():
    mb.showinfo("About", '''
    simple calculator app, using tkinter to create the GUI
    author : matthew tweedy
    ''')

# creating GUI elements
def buildMenu(parent):
    menus = (
        ("Help", evHelp),
        ("About", evAbout)
    )

    menubar = tk.Menu(parent)
    for menu in menus:
        m = tk.Menu(parent)
        m.add_command(label=menu[0], command=menu[1])

    return menubar

# calculation display
display = tk.Label(top, text=calc, border=1, padx=10, pady=25, font='Aerial 17 bold')
display.pack(anchor="n", fill="x", expand=True)

def buildCalculator(parent):

    outer = tk.Frame(parent, border=5, relief="flat")
    upperInner = tk.Frame(outer)
    upperInner.pack()
    inner = tk.Frame(outer)
    inner.pack()

    numbers = [7, 8, 9, 4, 5, 6, 1, 2, 3]
    count = 0

    for col in range(2):
        if col == 0:
            cell = tk.Button(upperInner, text=operators[6], width="17", height="3", font='Aerial 12 bold', command=lambda t=operators[6] : evClick(t))
        elif col == 1:
            cell = tk.Button(upperInner, text=operators[7], width="17", height="3", font='Aerial 12 bold', command=lambda t=operators[7] : evClick(t))
        cell.grid(row=1, column=col)


    # buttons
    for row in range(4):
        for col in range(4):

            number = numbers[count]
            # create buttons, filling in with numbers
            cell = tk.Button(inner, text=number, width="8", height="3", font='Aerial 12 bold', command=lambda t=number : evClick(t))
            if row != 3 and col == 3: # if the button is in the 4th col, fill with operator instead
                cell = tk.Button(inner, text=operators[row], width="8", height="3", font='Aerial 12 bold', command=lambda t=operators[row] : evClick(t))
                count -= 1
            count = (count+1) if count < 8 else 0

            # on the last row, fill only first col with num, rest with operators
            if row == 3 and col == 0:
                cell = tk.Button(inner, text="0", width="8", height="3", font='Aerial 12 bold', command=lambda t="0" : evClick(t))
            elif row == 3:
                cell = tk.Button(inner, text=operators[col+2], width="8", height="3", font='Aerial 12 bold', command=lambda t=operators[col+2] : evClick(t))
            cell.grid(row=row, column=col)
    return outer

mbar = buildMenu(top)
top['menu'] = mbar

calculator = buildCalculator(top)
calculator.pack()

mbar = buildMenu(top)
top['menu'] = mbar

def evClick(text):
    global calc
    global lastAnswer

    try:
        buttonClicked = int(text)
        display['text'] = concatNumber(buttonClicked)
    except ValueError:
        if text == "AC":
            evAC()
            display['text'] = calc
        elif text == "+":
            evAdd()
            display['text'] = calc
        elif text == "-":
            evSub()
            display['text'] = calc
        elif text == "x":
            evMultiply()
            display['text'] = calc
        elif text == "÷":
            evDivide()
            display['text'] = calc
        elif text == "=":
            lastAnswer = evCalculate()
            display['text'] = calc

tk.mainloop()