import re
import tkinter
from tkinter import messagebox

res = ''  # declaring a global variable res

font_properties = 'Calibri 15 bold'  # declaring a global font properties for buttons
# font_properties = 'TimesNewRoman 10 italic'

font_property_main = 'Calibri 18 bold'  # declaring a global font properties for calc_field


def add_digit(digit):  # addition digit (0-9) and point '.'
    # print(digit)
    value = calc_field.get()  # read calculation field

    # example without "res" argument
    # if (value[0] == '0' or value[0] == '') and len(value) == 1:
    #     if digit == '.':
    #         value = '0'
    #     else:
    #         value = value[1:]

    global res
    if value == res:  # case when new calculation starts...
        if digit == '.':  # ... from a dot
            value = '0'
        else:
            value = ''  # ... from a digit

    # case with two dots in calc.field
    elif re.split(r'[+\-/×]', value)[-1].count('.') >= 1 and digit == '.':
        digit = ''

    # case when in empty calc.field new float digit starts with dot '.' and not a zero '0'
    elif (value[0] == '0' or value[0] == '') and len(value) == 1:
        if digit == '.':
            value = '0'
        else:
            value = value[1:]

    # case when new float digit starts with dot '.' and not a zero '0'
    elif (value[-1] in '+-/' or value[-1] == '\u00D7') and digit == '.':
        value = value + '0'

    # refresh calc.field with new variables
    calc_field['state'] = tkinter.NORMAL  # unlock the calc.field
    calc_field.delete(0, tkinter.END)  # clear the input field from any data
    calc_field.insert(0, value + digit)  # input new variables into calc.field
    calc_field['state'] = tkinter.DISABLED  # lock the calc.field


def add_simple_operation(operation):
    value = calc_field.get()  # read calculation field
    # addition operation symbols
    if value[-1] in '-+/.' or value[-1] == '\u00D7':  # case with addition more than one operation symbol
        value = value[:-1]
    elif '+' in value or '-' in value or '/' in value or '\u00D7' in value:  # get result before add another operation
        result()
        value = calc_field.get()

    # refresh calc.field with new variables
    calc_field['state'] = tkinter.NORMAL  # unlock the calc.field
    calc_field.delete(0, tkinter.END)  # clear the input field from any data
    calc_field.insert(0, value + operation)  # input new variables into calc.field
    calc_field['state'] = tkinter.DISABLED  # lock the calc.field


def add_special_operation(operation):
    global res
    value = calc_field.get()  # read calculation field
    if operation == '1/x':
        if value == '0':
            messagebox.showinfo('Error!', 'Division by zero!')  # call message with an error
        else:
            value = str((1 / float(value)))
            res = value
    elif operation == 'x\u00B2':  # get power of two
        value = value + '**2'
    elif operation == '\u221A':  # get square root
        value = value + '**0.5'

    try:  # get rid of extra zeros in a float
        value = eval(value)
        if value % 1 == 0:
            value = str(int(value))
        else:
            value = str(float(value))
    except ZeroDivisionError:
        messagebox.showinfo('Error!', 'Division by zero!')

    # refresh calc.field with new variables
    calc_field['state'] = tkinter.NORMAL  # unlock the calc.field
    calc_field.delete(0, tkinter.END)  # clear the input field from any data
    calc_field.insert(0, value)  # input new variables into calc.field
    calc_field['state'] = tkinter.DISABLED  # lock the calc.field
    res = value


def backspace_action():
    value = calc_field.get()  # read calculation field
    global res
    if value == res or len(value) == 1:  # case when calc.field has one symbol or last result
        value = '0'
    elif len(value) > 1:  # del by one symbol
        value = value[:-1]

    # refresh calc.field with new variables
    calc_field['state'] = tkinter.NORMAL  # unlock the calc.field
    calc_field.delete(0, tkinter.END)  # clear the input field from any data
    calc_field.insert(0, value)  # input new variables into calc.field
    calc_field['state'] = tkinter.DISABLED  # lock the calc.field


def result():
    value = calc_field.get().replace('\u00D7', '*')  # replace multiply symbol 'x' for '*'
    if value[-1] in '+-/*':
        value = value + value[:-1]

    global res

    try:  # get rid of extra zeros in a float
        value = eval(value)
        if value % 1 == 0:
            value = str(int(value))
        else:
            value = str(float(value))
    except ZeroDivisionError:
        value = value[:-1]
        messagebox.showinfo('Error!', 'Division by zero!')  # call message with an error
    # refresh calc.field with new variables
    calc_field['state'] = tkinter.NORMAL  # unlock the calc.field
    calc_field.delete(0, tkinter.END)  # clear the input field from any data
    calc_field.insert(0, value)  # input new variables into calc.field
    calc_field['state'] = tkinter.DISABLED  # lock the calc.field
    res = value  # assigning a new value to result


def clear():
    # clear the input field from any data
    calc_field['state'] = tkinter.NORMAL  # unlock the calc.field
    calc_field.delete(0, tkinter.END)  # clear the input field from any data
    calc_field.insert(0, '0')  # input zero '0' into calc.field
    calc_field['state'] = tkinter.DISABLED  # lock the calc.field


def keyboard_press(event):
    # print(repr(event.char))
    if event.char.isdigit():
        add_digit(event.char)
    elif event.char in '+-/.':
        add_simple_operation(event.char)
    elif event.char == '*':
        add_simple_operation('\u00D7')
    elif event.char == '\r' or event.char == '=':
        result()
    elif event.char == '\b':
        backspace_action()
    elif event.char == '\x1b':
        clear()


def create_digit_button(digit):
    return tkinter.Button(text=digit,  # button text
                          bd=2,  # button edge thickness
                          font=font_properties,  # button font properties
                          fg='white',  # button font color
                          bg='#2c2c2e',  # button color
                          activebackground='#d4c9d1',  # pushed button color
                          # activebackground='green',  # pushed button color
                          command=lambda: add_digit(digit))  # called function


def create_simple_operation_button(operation):
    return tkinter.Button(text=operation,  # button text
                          bd=2,  # button edge thickness
                          font=font_properties,  # button font properties
                          fg='white',  # button font color
                          bg='#2c2c2e',  # button color
                          activebackground='#d4c9d1',  # pushed button color
                          command=lambda: add_simple_operation(operation))  # called function


def create_special_operation_button(operation):
    return tkinter.Button(text=operation,  # button text
                          bd=2,  # button edge thickness
                          font=font_properties,  # button font properties
                          fg='white',  # button font color
                          bg='#2c2c2e',  # button color
                          activebackground='#d4c9d1',  # pushed button color
                          command=lambda: add_special_operation(operation))  # called function


def create_result_button(operation):
    return tkinter.Button(text=operation,  # button text
                          bd=2,  # button edge thickness
                          font=font_properties,  # button font properties
                          fg='white',  # button font color
                          bg='#2c2c2e',  # pushed button color
                          activebackground='#d4c9d1',  # pushed button color
                          command=result)  # called function


def create_clear_button(operation):
    return tkinter.Button(text=operation,  # button text
                          bd=2,  # button edge thickness
                          font=font_properties,  # button font properties
                          fg='white',  # button font color
                          bg='#2c2c2e',  # pushed button color
                          activebackground='#d4c9d1',  # pushed button color
                          command=clear)  # called function


def create_backspace_button(operation):
    return tkinter.Button(text=operation,  # button text
                          bd=2,  # button edge thickness
                          font=font_properties,  # button font properties
                          fg='white',  # button font color
                          bg='#2c2c2e',  # pushed button color
                          activebackground='#d4c9d1',  # pushed button color
                          command=backspace_action)  # called function


# create the main window
window = tkinter.Tk()
window.config(bg='black', )
# window.config(bg='#d1cdcd')


# set title line
window.title("Calculator")
title_icon = tkinter.PhotoImage(file='calc_logo.png')
window.iconphoto(False, title_icon)

# bind keyboard
window.bind('<Key>', keyboard_press)

# set geometry behavior
window.geometry('252x355')
window.resizable(False, False)

# create calculation field
calc_field = tkinter.Entry(window,
                           justify=tkinter.RIGHT,
                           font=font_property_main,
                           )
calc_field.insert(0, '0')
calc_field['state'] = tkinter.DISABLED
calc_field.grid(row=0, column=0, columnspan=4, sticky='we', padx=4, pady=4)

# create digit buttons and dot
create_digit_button('0').grid(row=6, column=1, sticky='wens', padx=2, pady=2)
create_digit_button('1').grid(row=5, column=0, sticky='wens', padx=2, pady=2)
create_digit_button('2').grid(row=5, column=1, sticky='wens', padx=2, pady=2)
create_digit_button('3').grid(row=5, column=2, sticky='wens', padx=2, pady=2)
create_digit_button('4').grid(row=4, column=0, sticky='wens', padx=2, pady=2)
create_digit_button('5').grid(row=4, column=1, sticky='wens', padx=2, pady=2)
create_digit_button('6').grid(row=4, column=2, sticky='wens', padx=2, pady=2)
create_digit_button('7').grid(row=3, column=0, sticky='wens', padx=2, pady=2)
create_digit_button('8').grid(row=3, column=1, sticky='wens', padx=2, pady=2)
create_digit_button('9').grid(row=3, column=2, sticky='wens', padx=2, pady=2)
create_digit_button('.').grid(row=6, column=0, sticky='wens', padx=2, pady=2)  # add dot to digit

# create simple operation buttons
create_simple_operation_button('/').grid(row=2, column=3, sticky='wens', padx=2, pady=2)
create_simple_operation_button('\u00D7').grid(row=3, column=3, sticky='wens', padx=2, pady=2)  # multiply
create_simple_operation_button('-').grid(row=4, column=3, sticky='wens', padx=2, pady=2)
create_simple_operation_button('+').grid(row=5, column=3, sticky='wens', padx=2, pady=2)

# create special operation buttons
create_special_operation_button('1/x').grid(row=2, column=0, sticky='wens', padx=2, pady=2)  # one divided by variable
create_special_operation_button('x\u00B2').grid(row=2, column=1, sticky='wens', padx=2, pady=2)  # the power of two
create_special_operation_button('\u221A').grid(row=2, column=2, sticky='wens', padx=2, pady=2)  # sqrt action

# create clear buttons
create_clear_button('C').grid(row=1, column=0, sticky='wens', padx=2, pady=2, columnspan=2)  # clear all
create_backspace_button('DEL').grid(row=1, column=2, sticky='wens', padx=2, pady=2, columnspan=2)  # delete last symbol

# create result button
create_result_button('=').grid(row=6, column=2, sticky='wens', padx=2, pady=2, columnspan=2)

# configuration of row and columns
window.grid_columnconfigure(0, minsize=50)
window.grid_columnconfigure(1, minsize=50)
window.grid_columnconfigure(2, minsize=50)
window.grid_columnconfigure(3, minsize=50)
window.grid_rowconfigure(0, minsize=50)
window.grid_rowconfigure(1, minsize=50)
window.grid_rowconfigure(2, minsize=50)
window.grid_rowconfigure(3, minsize=50)
window.grid_rowconfigure(4, minsize=50)
window.grid_rowconfigure(5, minsize=50)
window.grid_rowconfigure(6, minsize=50)

# call main window
window.mainloop()
