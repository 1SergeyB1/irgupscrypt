from tkinter import *
from tkinter.filedialog import *
from generateKey import gen_key
from encrippt import enript_massage
from decript import decript_massage


def key_gen():
    window = Tk()
    window.title("Ключи")
    keys = gen_key()
    lbl = Label(window, text=keys)
    lbl.grid(column=0, row=0)
    with open('Ключи.txt', 'w', encoding='utf-8') as file:
        file.write(keys)


def file_encripter():
    def encript_function():
        with open('Зашифрованный файл.txt', 'w', encoding='utf-8') as file:
            text = enript_massage(e.get(), n.get(), askopenfilename())
            if text:
                file.write(text)
            else:
                file.write('Ошибка входныхданных')

    window = Tk()
    window.title("Зашифровать файл")
    lbl = Label(window, text='Введите e(первое число открытого ключа)')
    lbl.grid(column=0, row=0)
    e = Entry(window)
    e.grid(column=1, row=0)
    lbl = Label(window, text='Введите n(второе число открытого ключа)')
    lbl.grid(column=0, row=1)
    n = Entry(window)
    n.grid(column=1, row=1)
    Button(window, text='   защифровать файл    ', command=encript_function).grid(row=2, column=0)


def file_decripter():
    def encript_function():
        with open('Расшифрованный файл.txt', 'w', encoding='utf-8') as file:
            text = decript_massage(e.get(), n.get(), askopenfilename())
            if text:
                file.write(text)
            else:
                file.write('Ошибка входныхданных')

    window = Tk()
    window.title("Расшифровать файл")
    lbl = Label(window, text='Введите d(первое число закрытого ключа)')
    lbl.grid(column=0, row=0)
    e = Entry(window)
    e.grid(column=1, row=0)
    lbl = Label(window, text='Введите n(второе число закрытого ключа)')
    lbl.grid(column=0, row=1)
    n = Entry(window)
    n.grid(column=1, row=1)
    Button(window, text='   расшифровать файл    ', command=encript_function).grid(row=2, column=0)


root = Tk()
Button(root, text='   сгенерировать ключи     ', command=key_gen).grid(row=1, column=1)
Button(root, text='   Зашифровать файл    ', command=file_encripter).grid(row=1, column=2)
Button(root, text='   Расшифровать файл   ', command=file_decripter).grid(row=1, column=3)
root.mainloop()
