import tkinter as tk
from tkinter import *

numero1 = ''
numero2 = ''
adicao = FALSE
subtracao = FALSE
multiplicacao = FALSE
divisao = FALSE

root = Tk()
root.title('Sua calculadora')
root.geometry("408x355")
root.maxsize(408, 355)
root.minsize(408, 355)


root.configure(background='#282828')

e = Entry(root, width=15, borderwidth=4, relief=FLAT, fg='#FFFFFF',
          bg='#a7a28f', font=('futura', 25, 'bold'), justify=CENTER)
e.grid(
    row=0,
    column=0,
    columnspan=4,
    pady=2
)


def botao_click(num):
    e.insert(END, num)


def botao_adiciona():
    global numero1
    global adicao
    adicao = TRUE
    numero1 = e.get()
    e.delete(0, END)


def botao_subrai():
    global numero1
    global subtracao
    subtracao = TRUE
    numero1 = e.get()
    e.delete(0, END)


def botao_multiplica():
    global numero1
    global multiplicacao
    multiplicacao = TRUE
    numero1 = e.get()
    e.delete(0, END)


def botao_divide():
    global numero1
    global divisao
    divisao = TRUE
    numero1 = e.get()
    e.delete(0, END)


def botao_igual():
    global subtracao
    global divisao
    global multiplicacao
    global adicao
    numero2 = e.get()
    e.delete(0, END)
    if adicao == TRUE:
        e.insert(0, int(numero1) + int(numero2))
        adicao = FALSE
    if multiplicacao == TRUE:
        e.insert(0, int(numero1) * int(numero2))
        multiplicacao = FALSE
    if subtracao == TRUE:
        e.insert(0, int(numero1) - int(numero2))
        subtracao = FALSE
    if divisao == TRUE:
        e.insert(0, int(numero1) // int(numero2))
        divisao = FALSE


def botao_limpa():
    e.delete(0, END)


def botao_num(num, row, column):
    botao = Button(root,
                   text=num,
                   padx=40,
                   pady=20,
                   command=lambda: botao_click(num),
                   fg='#FFFFFF',
                   activebackground='#240046',
                   activeforeground='#FFFFFF',
                   bg='#282828',
                   relief=FLAT,
                   font=('futura', 12, 'bold'))
    botao.grid(row=row, column=column)


divide = Button(root,
                text='÷',
                padx=40,
                pady=20,
                command=botao_divide,
                fg='#FFFFFF',
                activebackground='#240046',
                activeforeground='#FFFFFF',
                bg='#320064',
                relief=FLAT,
                font=('futura', 12, 'bold'))
divide.grid(row=0, column=4)
# primeira fileira
botao_num(1, 1, 1)
botao_num(2, 1, 2)
botao_num(3, 1, 3)
multiplica = Button(root,
                    text='×',
                    padx=40,
                    pady=20,
                    command=botao_multiplica,
                    fg='#FFFFFF',
                    activebackground='#240046',
                    activeforeground='#FFFFFF',
                    bg='#320064',
                    relief=FLAT,
                    font=('futura', 12, 'bold'))
multiplica.grid(row=1, column=4)
# segunda fileira
botao_num(4, 2, 1)
botao_num(5, 2, 2)
botao_num(6, 2, 3)
menos = Button(root,
               text='-',
               padx=41.5,
               pady=20,
               command=botao_subrai,
               fg='#FFFFFF',
               activebackground='#240046',
               activeforeground='#FFFFFF',
               bg='#320064',
               relief=FLAT,
               font=('futura', 12, 'bold'))
menos.grid(row=2, column=4)
# terceira fileira
botao_num(7, 3, 1)
botao_num(8, 3, 2)
botao_num(9, 3, 3)
mais = Button(root,
              text='+',
              padx=39,
              pady=20,
              command=botao_adiciona,
              fg='#FFFFFF',
              activebackground='#240046',
              activeforeground='#FFFFFF',
              bg='#320064',
              relief=FLAT,
              font=('futura', 12, 'bold'))
mais.grid(row=3, column=4)
# quarta fileira
zero = Button(root,
              text='0',
              padx=91,
              pady=20,
              command=lambda: botao_click(0),
              fg='#FFFFFF',
              activebackground='#240046',
              activeforeground='#FFFFFF',
              bg='#282828',
              relief=FLAT,
              font=('futura', 12, 'bold'))
zero.grid(row=4, column=1, columnspan=2)
limpa = Button(root,
               text='C',
               padx=42,
               pady=20,
               command=botao_limpa,
               fg='#FFFFFF',
               activebackground='#240046',
               activeforeground='#FFFFFF',
               bg='#320064',
               relief=FLAT,
               font=('futura', 12, 'bold'))
limpa.grid(row=4, column=4)
igual = Button(root,
               text='=',
               padx=40,
               pady=20,
               command=botao_igual,
               fg='#FFFFFF',
               activebackground='#240046',
               activeforeground='#FFFFFF',
               bg='#320064',
               relief=FLAT,
               font=('futura', 12, 'bold'))
igual.grid(row=4, column=3)

root.mainloop()
