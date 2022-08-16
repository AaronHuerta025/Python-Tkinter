#Tkinter
# Modulo para crear interfaces graficas de usuarios

from tkinter import *
import os.path


class Programa:


    def __init__(self):
        self.title = "Master en Python"
        self.icon = './images/logo.ico' 
        self.icon_alt = './21-tkinter/images/logo.ico'
        self.size = "770x470"
        self.resisable = False


    def cargar(self):
        #Crear una ventana raiz
        ventana = Tk()
        self.ventana = ventana

        #Titulo de la ventana
        ventana.title(self.title)

        #Comprobar si existe un archivo
        ruta_icono = os.path.abspath(self.icon)
        # ruta_icono = os.path.abspath('./21-tkinter/imagenes/logo.ico')

        if not os.path.isfile(ruta_icono):
             ruta_icono = os.path.abspath(self.icon_alt)

        #Icono de la ventana
        ventana.iconbitmap(self.icon_alt)

        #Mostrar texto en el programa
        texto = Label(ventana, text=ruta_icono)
        texto.pack()

        #Cambiar el tamaño de la ventana
        ventana.geometry(self.size)

        #Bloquear el tamaño de la ventana
        if self.resisable:
            ventana.resizable(1,1)
        else:
             ventana.resizable(0,0)
    
    
    
    def addTexto(self,dato):
        texto = Label(self.ventana, text=dato)
        texto.pack()

    def mostrar(self):
         #Arrancar y mostrar la ventana hasta que se cierre
        self.ventana.mainloop()

       
#Instanciar el programa
programa = Programa()
programa.cargar()
programa.addTexto("Hola")
programa.mostrar()