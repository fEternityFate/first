import tkinter as tkinter


def add_digit(digit):  # Функция работы кнопок(+)
    value = calc.get()
    if value[0] == '0' and len(value) == 1:
        value = value[1:]
    calc.delete(0, tkinter.END)
    calc.insert(0, value+digit)


def add_operation(operation):  # Функция работы мат. знаков(+)
    value = calc.get()
    if value[-1] in '-+/*':
        value = value[:-1]
    elif '+' in value or '-' in value or '*' in value or '/' in value:
        calculate()
        value = calc.get()
    calc.delete(0, tkinter.END)
    calc.insert(0, value+operation)


def add_n_operation(operation):  # Функция возведение во 2 степень(+)
    value = calc.get()
    value = float(value)**2
    calc.delete(0, tkinter.END)
    calc.insert(0, value)


def calculate():  # Функция вывода результата(+)
    value = calc.get()
    if value[-1] in '+-/*':
        operation = float(value[-1])
        value = float(value[:-1])+operation+float(value[:-1])
    calc.delete(0, tkinter.END)
    calc.insert(0, eval(value))


def clear_one():  # Функция удаления последнего символа(+)
    value = calc.get()
    if (float(value) % 1) == 0:
        n_value = (float(value)-(float(value) % 1))//10.0
        calc.delete(0, tkinter.END)
        calc.insert(0, n_value)
    elif '.' in value:
        n_value = float(value)-(float(value) % 1)
        calc.delete(0, tkinter.END)
        calc.insert(0, n_value)
    elif value not in '.':
        n_value = int(value)//10
        calc.delete(0, tkinter.END)
        calc.insert(0, n_value)


def clear():  # Функция очистки поля(+)
    calc.delete(0, tkinter.END)
    calc.insert(0, 0)


def point(operation):  # Добавление точки(+-)
    value = calc.get()
    if '.' not in value:
        value = value + '.'
    calc.delete(0, tkinter.END)
    calc.insert(0, value)


def digit_buttom(digit):  # Функция кнопок(+)
    return tkinter.Button(text=digit, bd=5, font=('Arial', 13), command=lambda: add_digit(digit))


def oper_buttom(operation):  # Функция мат. символов(+)
    return tkinter.Button(text=operation, bd=5, font=('Arial', 13), fg='red', command=lambda: add_operation(operation))


def n_oper_buttom(operation):  # Функция мат. символов(+)
    return tkinter.Button(text=operation, bd=5, font=('Arial', 13), fg='red', command=lambda: add_n_operation(operation))


def operation_buttom(operation):  # Функция калькулятора(+)
    return tkinter.Button(text=operation, bd=5, font=('Arial', 13), fg='red', command=calculate)


def del_buttom(operation):  # Функция очистки одного символа(+)
    return tkinter.Button(text=operation, bd=5, font=('Arial', 13), fg='red', command=clear_one)


def clear_buttom(operation):  # Функция очистки поля(+)
    return tkinter.Button(text=operation, bd=5, font=('Arial', 13), fg='red', command=clear)


def add_point(operation):  # Функция добавления точки(+)
    return tkinter.Button(text=operation, bd=5, font=('Arial', 13), command=lambda: point(operation))


def press_key(event):  # Функция ввода символов с клавиатуры(+)
    print(repr(event.char))
    if event.char.isdigit():
        add_digit(event.char)
    elif event.char in '+-*/':
        add_operation(event.char)
    elif event.char == '\x08':
        clear_one()
    elif event.char in '.':
        point(event.char)
    elif event.char in 'c':
        clear()
    elif event.char == '\r':
        calculate()


# # Тело калькулятора
win = tkinter.Tk()
win.geometry(f'480x520+200+400')
win['bg'] = '#87ceeb'
win.title('Calculater')
win.bind('<Key>', press_key)

# # Поле ввода
calc = tkinter.Entry(win, justify=tkinter.RIGHT, font=('Arial', 15), width=15)
calc.insert(0, '0')
calc.grid(row=0, column=0, columnspan=5, stick='we')

# # Кнопки значений
digit_buttom('7').grid(row=1, column=0, stick='wens', padx=5, pady=5)
digit_buttom('8').grid(row=1, column=1, stick='wens', padx=5, pady=5)
digit_buttom('9').grid(row=1, column=2, stick='wens', padx=5, pady=5)
digit_buttom('4').grid(row=2, column=0, stick='wens', padx=5, pady=5)
digit_buttom('5').grid(row=2, column=1, stick='wens', padx=5, pady=5)
digit_buttom('6').grid(row=2, column=2, stick='wens', padx=5, pady=5)
digit_buttom('1').grid(row=3, column=0, stick='wens', padx=5, pady=5)
digit_buttom('2').grid(row=3, column=1, stick='wens', padx=5, pady=5)
digit_buttom('3').grid(row=3, column=2, stick='wens', padx=5, pady=5)
digit_buttom('0').grid(row=4, column=1, stick='wens', padx=5, pady=5)

# # Кнопки мат. символов
add_point('.').grid(row=4, column=2, stick='wens', padx=5, pady=5)
oper_buttom('+').grid(row=3, column=3, stick='wens', padx=5, pady=5)
oper_buttom('-').grid(row=3, column=4, stick='wens', padx=5, pady=5)
oper_buttom('*').grid(row=2, column=3, stick='wens', padx=5, pady=5)
oper_buttom('/').grid(row=2, column=4, stick='wens', padx=5, pady=5)
n_oper_buttom('^2').grid(row=1, column=3, stick='wens', padx=5, pady=5)

# # Кнопки очистки и вывода
clear_buttom('Clear').grid(row=4, column=0, stick='wens', padx=5, pady=5)
operation_buttom('=').grid(row=4, column=3, columnspan=2,
                           stick='wens', padx=5, pady=5)
del_buttom('Del').grid(row=1, column=4, stick='wens', padx=5, pady=5)

# # Размеры кнопок по ширине
win.grid_columnconfigure(0, minsize=95)
win.grid_columnconfigure(1, minsize=95)
win.grid_columnconfigure(2, minsize=95)
win.grid_columnconfigure(3, minsize=95)
win.grid_columnconfigure(4, minsize=95)

# # Размеры кнопок по высоте
win.grid_rowconfigure(1, minsize=120)
win.grid_rowconfigure(2, minsize=120)
win.grid_rowconfigure(3, minsize=120)
win.grid_rowconfigure(4, minsize=120)

win.mainloop()
