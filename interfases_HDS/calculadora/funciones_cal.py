from tkinter import *
def enviar_boton(valor,pantalla):
    anterior = pantalla.get()
    pantalla.delete(0,END)
    pantalla.insert(0,str(anterior)+str(valor))

def operacion(signo,pantalla):
    global num1
    global signo_op
    num1 = pantalla.get()
    num1=float(num1)
    pantalla.delete(0,END)
    signo_op = signo

def igual(pantalla):
    global num1
    num2 = pantalla.get()
    num2=float(num2)
    pantalla.delete(0,END)
    if signo_op == "+":
        pantalla.insert(0, num1 + float(num2))
    elif signo_op == "-":
        pantalla.insert(0, num1 - float(num2))
    elif signo_op == "/":
        pantalla.insert(0, num1 / float(num2))
    elif signo_op == "*":
        pantalla.insert(0, num1 * float(num2))

def limpiar_pantalla(pantalla):
    pantalla.delete(0,END)