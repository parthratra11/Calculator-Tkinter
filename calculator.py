from tkinter import *

base = Tk()
base.title('Calculator'); base.config(background = '#7A7A7A')

#! CHANGE IT BEFORE POSTING IT
icon_path = r'Projects\\calculator\\calculator-svg-png-icon-free-download-521113-onlinewebfontscom.png'
# icon_path = input('Enter the path of the saved icon image:')

base.iconphoto(False, PhotoImage(file = icon_path))

calc = Frame(base, borderwidth = 2); calc.grid(row = 0, column = 0, padx = 5, pady = 5, columnspan = 4)
temp_calc = Frame(calc, borderwidth = 2); temp_calc.grid(row = 0, column = 0, padx = 2, pady = 2, columnspan = 4)

operations_str, temp_operations_str, invalid_val, old_val, new_val, op, check_backspace, check_click = '', '', 'valid', '', '', '', 0, 0

def button_click(var):
    global operations_str, temp_operations_str, old_val, new_val, op, check_backspace, check_click

    if invalid_val == 'valid':

        if var == '.':
            temp_operations_str += '0.' if temp_operations_str == '' else '.'
            operations_str += '0.' if temp_operations_str == '0.' else '.'

            ent.delete(0, END); ent.insert(0, temp_operations_str)
            temp_operation = Label(calc, text = operations_str, width = 73, font = ('Bahnschrift', '8'), bg = '#A1A1A1', fg = 'black', borderwidth = 1, relief = SUNKEN, anchor = E); temp_operation.grid(row = 5, column = 0, columnspan = 4)

            new_val = temp_operations_str

        elif str(var) not in '+-x%':
                
            try:
                operations_str += str(var); temp_operations_str += str(var)

                if check_backspace == 1 or check_click == 1:
                    old_val = float(temp_operations_str)

                else:
                    new_val = float(temp_operations_str)

                ent.delete(0, END); ent.insert(0, temp_operations_str)
                temp_operation = Label(calc, text = operations_str, width = 73, font = ('Bahnschrift', '8'), bg = '#A1A1A1', fg = 'black', borderwidth = 1, relief = SUNKEN, anchor = E); temp_operation.grid(row = 5, column = 0, columnspan = 4)
            
            except:
                invalid_operation()

        else:
            if not temp_operations_str:
                invalid_operation()

            else:
                check_backspace, check_click = 0, 0
                operation(op)

                op, temp_operations_str = str(var), ''
                operations_str += f'0 {op} ' if operations_str[-1] == '.' else f' {op} '

                ent.delete(0, END)
                temp_operation = Label(calc, text = operations_str, width = 73, font = ('Bahnschrift', '8'), bg = '#A1A1A1', fg = 'black', borderwidth = 1, relief = SUNKEN, anchor = E); temp_operation.grid(row = 5, column = 0, columnspan = 4)

def operation(key):
    global old_val, new_val, op

    if not old_val:
        old_val, op = float(temp_operations_str), key

    else:
        new_val = float(temp_operations_str)
        old_val = temp_result(float(old_val), key, float(new_val))

    ent.delete(0, END); ent.insert(0, old_val)
    temp_operation = Label(calc, text = old_val, width = 73, font = ('Bahnschrift', '8'), bg = '#A1A1A1', fg = 'black', borderwidth = 1, relief = SUNKEN, anchor = E); temp_operation.grid(row = 5, column = 0, columnspan = 4)

def backspace():
    global operations_str, temp_operations_str, check_backspace

    if invalid_val == 'valid':
        check_backspace = 1

        operations_str = operations_str[-2::-1][::-1] if len(operations_str) > 0 else ''
        temp_operations_str = temp_operations_str[-2::-1][::-1] if len(temp_operations_str) > 0 else ''

        ent.delete(0, END); ent.insert(0, temp_operations_str)
        temp_operation = Label(calc, text = operations_str, width = 73, font = ('Bahnschrift', '8'), bg = '#A1A1A1', fg = 'black', borderwidth = 1, relief = SUNKEN, anchor = E); temp_operation.grid(row = 5, column = 0, columnspan = 4)    

def clear():
    global operations_str, temp_operations_str, invalid_val, old_val, new_val, ent, check_backspace, check_click

    operations_str, temp_operations_str, invalid_val, old_val, new_val, check_backspace, check_click = '', '', 'valid', '', '', 0, 0

    ent = Entry(temp_calc, bg = '#9B9B9B', fg = 'black', width = 26, font = ('Bahnschrift Light', '10', 'bold'), borderwidth = 4, justify=RIGHT); ent.grid(row = 0,column = 0, columnspan = 2)
    temp_operation = Label(calc, width = 73, font = ('Bahnschrift', '8'), bg = '#A1A1A1', fg = 'black', borderwidth = 1, relief = SUNKEN, anchor = E); temp_operation.grid(row = 5, column = 0, columnspan = 4)

def temp_result(temp_old_val, temp_operation_key, temp_new_val):
    global old_val

    result_var = 0

    if temp_new_val == 0 and temp_operation_key == '%':
        invalid_operation()
        result_var = 0
    
    elif temp_operation_key == '+':
        result_var = temp_old_val + temp_new_val

    elif temp_operation_key == '-':
        result_var = temp_old_val - temp_new_val

    elif temp_operation_key == 'x':
        result_var = temp_old_val * temp_new_val

    elif temp_operation_key == '%':
        result_var = temp_old_val / temp_new_val

    else:
        result_var = temp_old_val

    old_val = result_var

    return result_var

def result():
    global old_val, new_val, op, operations_str, temp_operations_str, check_click

    if old_val == '' or new_val == '':
        old_val = float(temp_operations_str)
        result = old_val

    else:
        result = temp_result(float(old_val), op, float(new_val))
        old_val, op, new_val, operations_str, temp_operations_str = result, '', '', str(result), str(result)

    check_click = 1
    ent.delete(0, END); ent.insert(0, operations_str)
    temp_operation = Label(calc, text = temp_operations_str, width = 73, font = ('Bahnschrift', '8'), bg = '#A1A1A1', fg = 'black', borderwidth = 1, relief = SUNKEN, anchor = E); temp_operation.grid(row = 5, column = 0, columnspan = 4)    

def invalid_operation():
    global invalid_val

    clear()
    invalid_val = 'invalid'

    ent = Entry(temp_calc, bg = '#9B9B9B', fg = 'black', width = 26, font = ('Bahnschrift Light', '10', 'bold'), borderwidth = 4, justify=CENTER); ent.grid(row = 0,column = 0, columnspan = 2)
    ent.insert(0, 'Invalid Operation !')
    temp_operation = Label(calc, width = 73, text = 'Invalid Operation !', font = ('Bahnschrift', '8'), bg = '#A1A1A1', fg = 'black', borderwidth = 1, relief = SUNKEN, anchor = E); temp_operation.grid(row = 5, column = 0, columnspan = 4)

ent = Entry(temp_calc, bg = '#9B9B9B', fg = 'black', width = 26, font = ('Bahnschrift Light', '10', 'bold'), borderwidth = 4, justify=RIGHT); ent.grid(row = 0,column = 0, columnspan = 2)

button_7 = Button(temp_calc, width = 11, pady = 10, borderwidth = 2, bg = '#CBCBCB', fg = 'black', font = ('Calibri Light (Headings)', '11', 'bold'), text = '7', command = lambda: button_click('7')); button_7.grid(row = 1, column = 0)
button_8 = Button(temp_calc, width = 11, pady = 10, borderwidth = 2, bg = '#CBCBCB', fg = 'black', font = ('Calibri Light (Headings)', '11', 'bold'), text = '8', command = lambda: button_click('8')); button_8.grid(row = 1, column = 1)
button_9 = Button(temp_calc, width = 11, pady = 10, borderwidth = 2, bg = '#CBCBCB', fg = 'black', font = ('Calibri Light (Headings)', '11', 'bold'), text = '9', command = lambda: button_click('9')); button_9.grid(row = 1, column = 2)

button_4 = Button(temp_calc, width = 11, pady = 10, borderwidth = 2, bg = '#CBCBCB', fg = 'black', font = ('Calibri Light (Headings)', '11', 'bold'), text = '4', command = lambda: button_click('4')); button_4.grid(row = 2, column = 0)
button_5 = Button(temp_calc, width = 11, pady = 10, borderwidth = 2, bg = '#CBCBCB', fg = 'black', font = ('Calibri Light (Headings)', '11', 'bold'), text = '5', command = lambda: button_click('5')); button_5.grid(row = 2, column = 1)
button_6 = Button(temp_calc, width = 11, pady = 10, borderwidth = 2, bg = '#CBCBCB', fg = 'black', font = ('Calibri Light (Headings)', '11', 'bold'), text = '6', command = lambda: button_click('6')); button_6.grid(row = 2, column = 2)

button_1 = Button(temp_calc, width = 11, pady = 10, borderwidth = 2, bg = '#CBCBCB', fg = 'black', font = ('Calibri Light (Headings)', '11', 'bold'), text = '1', command = lambda: button_click('1')); button_1.grid(row = 3, column = 0)
button_2 = Button(temp_calc, width = 11, pady = 10, borderwidth = 2, bg = '#CBCBCB', fg = 'black', font = ('Calibri Light (Headings)', '11', 'bold'), text = '2', command = lambda: button_click('2')); button_2.grid(row = 3, column = 1)
button_3 = Button(temp_calc, width = 11, pady = 10, borderwidth = 2, bg = '#CBCBCB', fg = 'black', font = ('Calibri Light (Headings)', '11', 'bold'), text = '3', command = lambda: button_click('3')); button_3.grid(row = 3, column = 2)

button_0 = Button(temp_calc, width = 11, pady = 10, borderwidth = 2, bg = '#CBCBCB', fg = 'black', font = ('Calibri Light (Headings)', '11', 'bold'), text = '0', command = lambda: button_click('0')); button_0.grid(row = 4, column = 0)

button_back = Button(temp_calc, width= 12, padx = 2, pady = 2, borderwidth = 3, bg = '#A1A1A1', fg = 'black', font = ('Calibri Light (Headings)', '10', 'bold'), text = '<<', command = backspace); button_back.grid(row = 0, column = 2)
button_clr = Button(temp_calc, width= 12, padx = 2, pady = 2, borderwidth = 3, bg = '#A1A1A1', fg = 'black', font = ('Calibri Light (Headings)', '10', 'bold'), text = 'Clear', command = clear); button_clr.grid(row = 0, column = 3)
button_add = Button(temp_calc, width = 11, pady = 10, borderwidth = 2, bg = '#B0B0B0', fg = 'black', font = ('Calibri Light (Headings)', '11', 'bold'), text = '+', command = lambda: button_click('+')); button_add.grid(row = 1, column = 3)
button_subtract = Button(temp_calc, width = 11, pady = 10, borderwidth = 2, bg = '#B0B0B0', fg = 'black', font = ('Calibri Light (Headings)', '11', 'bold'), text = '-', command = lambda: button_click('-')); button_subtract.grid(row = 2, column = 3)
button_multiply = Button(temp_calc, width = 11, pady = 10, borderwidth = 2, bg = '#B0B0B0', fg = 'black', font = ('Calibri Light (Headings)', '11', 'bold'), text = 'x', command = lambda: button_click('x')); button_multiply.grid(row = 4, column = 1)
button_divide = Button(temp_calc, width = 11, pady = 10, borderwidth = 2, bg = '#B0B0B0', fg = 'black', font = ('Calibri Light (Headings)', '11', 'bold'), text = '%', command = lambda: button_click('%')); button_divide.grid(row = 4, column = 2)
button_decimal = Button(temp_calc, width = 11, pady = 10, borderwidth = 2, bg = '#B0B0B0', fg = 'black', font = ('Calibri Light (Headings)', '11', 'bold'), text = '.', command = lambda: button_click('.')); button_decimal.grid(row = 3, column = 3)
button_equal = Button(temp_calc, width = 11, pady = 9, borderwidth = 3, bg = '#9B9B9B', fg = 'black', font = ('Calibri Light (Headings)', '11', 'bold'), text = '=', command = result); button_equal.grid(row = 4, column = 3)

temp_operation = Label(calc, width = 73, font = ('Bahnschrift', '8'), bg = '#A1A1A1', fg = 'black', borderwidth = 1, relief = SUNKEN, anchor = E); temp_operation.grid(row = 5, column = 0, columnspan = 4)

base.mainloop()