from tkinter import *

ventana = Tk()
ventana.geometry("700x500")


texto = Label(ventana, text="Bienvenido  a mi programa")
texto.config(

    fg="white",  # Color de letra
    bg="black",  # Color de fondo tambien podemos poner los colores en hexadecional como #000000
    padx=50,  # Genera un padding
    pady=20,
    font=("Consolas", 30),  # Tipo de letra
    justify=RIGHT  # Justificar el texto
)
texto.pack(side=TOP)#LEFT RIGTH BUTTON

texto = Label(ventana, text="Soy Aarón Huerta")
texto.config(
    width=20,
    height=2,
    bg="orange",
    font=("Arial", 18),
    padx=10,
    pady=10,
    # cursor = "arrow" hay muchos más
    cursor = "circle"

)
texto.pack(side=TOP, fill=X,expand=YES)#anchor=E



texto = Label(ventana, text="Basico 1")
texto.config(
    width=6,
    height=4,
    bg="red",
    font=("Arial", 18),
    padx=10,
    pady=10,
    # cursor = "arrow" hay muchos más
    cursor = "spider" #circle

)
texto.pack(side=LEFT, fill=X,expand=YES)


texto = Label(ventana, text="Basico 2")
texto.config(
    width=6,
    height=4,
    bg="blue",
    font=("Arial", 18),
    padx=10,
    pady=10,
    # cursor = "arrow" hay muchos más
    cursor = "spider" #circle

)
texto.pack(side=LEFT, fill=X,expand=YES)




texto = Label(ventana, text="Basico 3")
texto.config(
    width=6,
    height=4,
    bg="yellow",
    font=("Arial", 18),
    padx=10,
    pady=10,
    # cursor = "arrow" hay muchos más
    cursor = "spider" #circle

)
texto.pack(side=LEFT, fill=X,expand=YES)


ventana.mainloop()
