# -*- coding: utf-8 -*-
from tkinter import *
from tkinter.ttk import Combobox
import subprocess
import os
import shutil
from pathlib import Path


def run():
    dir = os.path.abspath(os.curdir)
    p = dir[0:len(dir) - 8]
    asterios = p + "Asterios.exe /autoplay"
    subprocess.Popen(asterios, shell=True, stdout=subprocess.PIPE, encoding='utf-8')

    window.destroy()
    return


def stop():
    window.destroy()
    return

def clicked():
    lbl.configure(text=combo.get())
    name = combo.get()
    shutil.copy(r"" + name + ".ini", r"AsteriosGame.ini")


    window.mainloop()
    return


def adde():
    pr = "Добавил {}".format(txt.get())
    res = format(txt.get())
    a = lbl.configure(text=pr)
    # 2. Открыть файл для записи
    f = open('char.txt', 'a')
    # 3. Цикл записи строк

    f.write(res + '\n')
    # 4. Закрыть файл
    f.close()
    shutil.copy(r"AsteriosGame.ini", r"" + res + ".ini")





    return

def lst():
    f = open('char.txt', 'rt')

    # 6. Сформировать новый список
    lst2 = []  # сначала пустой список

    # 7. Реализовать обход файла по строкам и считать числа.
    # Для чтения строк используется итератор файла.
    for s in f:
        # Убрать последний символ '\n' из s
        s = s.rstrip()

        # Добавить строку s в список lst2
        lst2 = lst2 + [s]

    # 8. Вывести список lst2 для контроля

    # 9. Закрыть файл - необязательно
    f.close()

    return lst2
def delet():
    name = format(combo.get())


    lst=lsts
    print(lst)
    lstsd=lst.remove(name)
    path = os.path.join(os.path.abspath(os.path.dirname(__file__)), name+'.ini')
    os.remove(path)
    path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'char.txt')
    os.remove(path)
    f = open('char.txt', 'a')



    # 7. Реализовать обход файла по строкам и считать числа.
    # Для чтения строк используется итератор файла.
    for i in lst:
        s = str(i)  # конвертировать элемент списка в строку
        f.write(s + '\n')  # записать число в строку

    # 8. Вывести список lst2 для контроля

    # 9. Закрыть файл - необязательно
    f.close()
    return
def combo():
    global combo
    lsts=lst()
    combo = Combobox(window)
    combo['values'] = lsts
    # combo.current(1)  # установите вариант по умолчанию
    combo.grid(column=0, row=5)
    combo.get()
    return

lsts=lst()
window = Tk()
window.title("Запускатор Ver. Alpha 2")
C = Canvas(window, bg="blue")
filename = PhotoImage(file = "img\\12.png")
background_label = Label(window, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
window.resizable(width=False, height=False)

btn = Button(window, text="Выбор персонажа", command=clicked,font='Times 15' )
btn2 = Button(window, text="Записать нового песонажа", command=adde,font='Times 15')
btn3 = Button(window, text="Обновить список", command=combo,font='Times 15')
btn4 = Button(window, text="Удалить персонажа из списка ", command=delet,font='Times 15')
btn5 = Button(window, text="Запустить игру ", command=run,font='Times 15')
lbl = Label(window, text="Введите имя персонажа",font='Times 15')
lbl.grid(column=10, row=0)
txt = Entry(window, width=20)
txt.grid(column=10, row=3)

lbl = Label(window, text='Веберите персонажа', font='Times 20' )
lbl.grid(column=0, row=3)
combo()
btn.grid(column=3, row=5)
btn2.grid(column=10, row=5)
btn3.grid(column=20, row=5)
btn4.grid(column=10, row=10)
btn5.grid(column=0, row=10)
window.mainloop()
