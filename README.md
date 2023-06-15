# tkinter-calculator
This is a simple calculator using tkinter library to create a GUI application. Also contains a more simple cmd line interface if preferable.
Handles nearly all bad input, still ironing out smaller quirks.

# calc GUI logic for inputting numbers and the options:
    # calc default string = "0"
    # any number input will overwrite default
    # any operation pressed while default will take x as 0
    # if operation pressed when last char in calc string = operation:
    #       don't change calc string
    # parse calc string to get x, y, op (split on " ")
    #       and pass onto logic
    # pressing "=" button will then call correct logic function/method
