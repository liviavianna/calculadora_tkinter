import tkinter as tk
from tkinter import *

numero1 = ''
numero2 = ''
adicao = ''
subtracao = ''
multiplicacao = ''
divisao = ''

root = Tk()
root.title('Sua calculadora')
root.geometry("408x355")
root.maxsize(408,355)
root.minsize(408,355)


root.configure(background='#282828')

e = Entry(root, width=15, borderwidth=4, relief=FLAT, fg='#FFFFFF', bg='#a7a28f', font=('futura', 25, 'bold'), justify=CENTER)
e.grid(
  row=0,
  column=0,
  columnspan=4,
  pady=2
)


def botaoClick(num):
  atual = e.get()
  e.delete(0, END)
  e.insert(0, atual + str(num))
  
def botaoAdiciona():
  global numero1
  global adicao
  adicao = 'adicao'
  numero1 = e.get()
  e.delete(0, END)
def botaoSubtrai():
  global numero1
  global subtracao
  subtracao = 'subtracao'
  numero1 = e.get()
  e.delete(0, END)
def botaoMultiplica():
  global numero1
  global multiplicacao
  multiplicacao = 'multiplicacao'
  numero1 = e.get()
  e.delete(0, END)
def botaoDivide():
  global numero1
  global divisao
  divisao = 'divisao'
  numero1 = e.get()
  e.delete(0, END)
def botaoIgual():
  if adicao == 'adicao':
    numero2 = e.get()
    e.delete(0, END)
    e.insert(0, int(numero1) + int(numero2))
  elif multiplicacao == 'multiplicacao':
    numero2 = e.get()
    e.delete(0, END)
    e.insert(0, int(numero1) * int(numero2))
  elif subtracao == 'subtracao':
    numero2 = e.get()
    e.delete(0, END)
    e.insert(0, int(numero1) - int(numero2))
  elif divisao == 'divisao':
    numero2 = e.get()
    e.delete(0, END)
    e.insert(0, int(numero1) // int(numero2))
def botaoLimpa():
  e.delete(0, END)
divide = Button(root,
                 text='/',
                 padx=42,
                 pady=20,
                 command=botaoDivide,
                 fg='#FFFFFF',
                 activebackground='#240046',
                 activeforeground='#FFFFFF',
                 bg='#320064',
                 relief=FLAT,
                 font=('futura', 12, 'bold'))
divide.grid(row=0, column=4) 
#primeira fileira
um = Button(root,
            text='1',
            padx=40,
            pady=20,
            command=lambda: botaoClick(1),
            fg='#FFFFFF',
            activebackground='#240046',
            activeforeground='#FFFFFF',
            bg='#282828',
            relief=FLAT,
            font=('futura', 12, 'bold'))
um.grid(row=1, column=1)
dois = Button(root,
              text='2',
              padx=40,
              pady=20,
              command=lambda: botaoClick(2),
              fg='#FFFFFF',
              activebackground='#240046',
              activeforeground='#FFFFFF',
              bg='#282828',
              relief=FLAT,
              font=('futura', 12, 'bold'))
dois.grid(row=1, column=2)
tres = Button(root,
              text='3',
              padx=40,
              pady=20,
              command=lambda: botaoClick(3),
              fg='#FFFFFF',
              activebackground='#240046',
              activeforeground='#FFFFFF',
              bg='#282828',
              relief=FLAT,
              font=('futura', 12, 'bold'))
tres.grid(row=1, column=3)
multiplica = Button(root,
                text='x',
                padx=40,
                pady=20,
                command=botaoMultiplica,
                fg='#FFFFFF',
                activebackground='#240046',
                activeforeground='#FFFFFF',
                bg='#320064',
                relief=FLAT,
                font=('futura', 12, 'bold'))
multiplica.grid(row=1, column=4)
#segunda fileira
quatro = Button(root,
                text='4',
                padx=40,
                pady=20,
                command=lambda: botaoClick(4),
                fg='#FFFFFF',
                activebackground='#240046',
                activeforeground='#FFFFFF',
                bg='#282828',
                relief=FLAT,
                font=('futura', 12, 'bold'))
quatro.grid(row=2, column=1)
cinco = Button(root,
               text='5',
               padx=40,
               pady=20,
               command=lambda: botaoClick(5),
               fg='#FFFFFF',
               activebackground='#240046',
               activeforeground='#FFFFFF',
               bg='#282828',
               relief=FLAT,
               font=('futura', 12, 'bold'))
cinco.grid(row=2, column=2)
seis = Button(root,
              text='6',
              padx=40,
              pady=20,
              command=lambda: botaoClick(6),
              fg='#FFFFFF',
              activebackground='#240046',
              activeforeground='#FFFFFF',
              bg='#282828',
              relief=FLAT,
              font=('futura', 12, 'bold'))
seis.grid(row=2, column=3)
menos = Button(root,
                   text='-',
                   padx=41.5,
                   pady=20,
                   command=lambda: botaoSubtrai(),
                   fg='#FFFFFF',
                   activebackground='#240046',
                   activeforeground='#FFFFFF',
                   bg='#320064',
                   relief=FLAT,
                   font=('futura', 12, 'bold'))
menos.grid(row=2, column=4)
#terceira fileira
sete = Button(root,
              text='7',
              padx=40,
              pady=20,
              command=lambda: botaoClick(7),
              fg='#FFFFFF',
              activebackground='#240046',
              activeforeground='#FFFFFF',
              bg='#282828',
              relief=FLAT,
              font=('futura', 12, 'bold'))
sete.grid(row=3, column=1)
oito = Button(root,
              text='8',
              padx=40,
              pady=20,
              command=lambda: botaoClick(8),
              fg='#FFFFFF',
              activebackground='#240046',
              activeforeground='#FFFFFF',
              bg='#282828',
              relief=FLAT,
              font=('futura', 12, 'bold'))
oito.grid(row=3, column=2)
nove = Button(root,
              text='9',
              padx=40,
              pady=20,
              command=lambda: botaoClick(9),
              fg='#FFFFFF',
              activebackground='#240046',
              activeforeground='#FFFFFF',
              bg='#282828',
              relief=FLAT,
              font=('futura', 12, 'bold'))
nove.grid(row=3, column=3)
mais = Button(root,
               text='+',
               padx=39,
               pady=20,
               command=botaoAdiciona,
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
              command=lambda: botaoClick(0),
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
                 command=botaoLimpa,
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
               command=botaoIgual,
               fg='#FFFFFF',
               activebackground='#240046',
               activeforeground='#FFFFFF',
               bg='#320064',
               relief=FLAT,
               font=('futura', 12, 'bold'))
igual.grid(row=4, column=3)

root.mainloop()
