from tkinter import *
from tkinter import messagebox as MessageBox



ventana = Tk()
ventana.config(bd=70)


def sacarAlerta():
    # MessageBox.showinfo("Alerta", "Hola soy Aarón")
    # MessageBox.showwarning("Alerta", "Hola soy Aarón")
    MessageBox.showerror("Alerta", "Hola soy Aarón")

Button(ventana, text="Mostrar alerta!!!", command=sacarAlerta).pack()






def salir(nombre):
    resultado = MessageBox.askquestion("Salir", "¿Quieres continuar en la aplicacion?")
    if resultado != "yes":
        MessageBox.showinfo("Chao!!!",f"Adios {nombre}" )
        ventana.destroy()

Button(ventana, text="Salir", command=lambda:salir("Aarón")).pack()



ventana.mainloop()