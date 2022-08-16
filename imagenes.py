from tkinter import *


ventana = Tk()
ventana.geometry("700x600")
ventana.config(bg="blue")
ventana.title("Ejemplo de imagenes")

#Creamos la imagen
imagenL=PhotoImage(file="Anchor.png")
labelIamgen = Label(ventana, image=imagenL).place(x=100,y=100)


ventana.mainloop()