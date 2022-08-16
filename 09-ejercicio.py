"""
CALCULADORA:
- DOS CAMPOS DE TEXTO
- 4 BOTONES PARA LAS OPERACIONES
- MOSTRAR EL RESULTADO
"""

from tkinter import *
from tkinter import messagebox

ventana = Tk()
ventana.title("Ejercicio completo con Tkinter |Calculadora")
ventana.geometry("400x400")
ventana.config(bd=25)


def cfloat(numero):
    try:
        result = float(numero)
    except:
        result=0
        messagebox.showerror("Error", "Introduce bien los datos")
    return result


def sumar():
    resultado.set(cfloat(numero.get())+cfloat(numero2.get()))
    mostrarResultado()


def restar():
    resultado.set(cfloat(numero.get())-cfloat(numero2.get()))
    mostrarResultado()


def multiplicar():
    resultado.set(cfloat(numero.get())*cfloat(numero2.get()))
    mostrarResultado()


def dividir():
    resultado.set(cfloat(numero.get())/cfloat(numero2.get()))
    mostrarResultado()


numero = StringVar()
numero2 = StringVar()
resultado = StringVar()


def mostrarResultado():
    messagebox.showinfo("Resultado: ", f"El resultado es: {resultado.get()}")
    numero.set("")
    numero2.set("")


marco = Frame(ventana, width=350, height=200)
marco.config(
    padx=15,
    pady=15,
    bd=5,
    relief=SOLID,
)
marco.pack(side=TOP, anchor=CENTER)
marco.pack_propagate(False)


Label(marco, text="Primer número: ").pack()
Entry(marco, textvariable=numero,  justify="center").pack()


Label(marco, text="Segundo Numero: ").pack()
Entry(marco, textvariable=numero2, justify="center").pack()


Label(marco, text="").pack()

Button(marco, text="Sumar", command=sumar).pack(
    side="left", fill=X, expand=YES)
Button(marco, text="Restar", command=restar).pack(
    side="left", fill=X, expand=YES)
Button(marco, text="Multiplicar", command=multiplicar).pack(
    side="left", fill=X, expand=YES)
Button(marco, text="Dividir", command=dividir).pack(
    side="left", fill=X, expand=YES)

ventana.mainloop()
