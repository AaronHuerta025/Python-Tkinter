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
texto.pack()

texto = Label(ventana, text="Soy Aarón Huerta")
texto.config(
    width=200,
    height=4,
    bg="orange",
    font=("Arial", 18),
    padx=10,
    pady=10,
    # cursor = "arrow" hay muchos más
    cursor = "circle"

)
texto.pack(anchor=W)


def pruebas(nombre, apellidos, pais):
    return f"Hola {nombre} {apellidos} veo que eres de {pais}"



texto = Label(ventana, text=pruebas(nombre ="Aarón", apellidos= "Huerta", pais="México"))
texto.config(
    width=400,
    height=400,
    bg="red",
    font=("Arial", 18),
    padx=10,
    pady=10,
    # cursor = "arrow" hay muchos más
    cursor = "spider" #circle

)
texto.pack(anchor=NW)

ventana.mainloop()
