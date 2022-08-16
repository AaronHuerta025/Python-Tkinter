from tkinter import*
ventana = Tk()
ventana.geometry("700x400")
ventana.title("Formularios | Master Python")


# Texto encabezado
encabezado = Label(ventana,text="Formularios con tkinter y Aarón Huerta")
encabezado.config(
    fg="white",
    bg="darkgray",
    font=("Open Sans", 18),
    padx=10,
    pady=10
)
encabezado.grid(row=0, column=0,columnspan=13, sticky=W)

#Label para el campo (NOMBRE)
label = Label(ventana, text="Nombre")
label.grid(row=1, column=0, pady=5, sticky=W, padx=5)

#Campo texto (NOMBRE)
campo_texto = Entry(ventana)
campo_texto.grid(row = 1, column=1, padx=5, pady=5, sticky=W)
campo_texto.config(justify="right", state="normal")# Forma en la que entra eel texto a escribir


#Label para el campo (apellidos)
label = Label(ventana, text="Apellidos")
label.grid(row=4, column=0, pady=5, sticky=W, padx=5)

#Campo texto (apellidos)
campo_texto = Entry(ventana)
campo_texto.grid(row = 4, column=1, padx=5, pady=5, sticky=W)
campo_texto.config(justify="right", state="normal")



#Label para el campo (descripcion)
label = Label(ventana, text="Descripción")
label.grid(row=6, column=0, pady=5, sticky=N, padx=5)

#Campo texto (descripcion)
campo_grande = Text(ventana)
campo_grande.grid(row = 6, column=1, padx=5, pady=5, sticky=W)
campo_grande.config(
    
    width=30, 
    height=5,
    font=("Arial",12),
    padx=15,
    pady=15
 ) 

# Boton
Label(ventana).grid(row=7, column=1) # Label separador

boton = Button(ventana, text="Enviar")
boton.grid(row=8, column=1, sticky=W)
boton.config(padx=15, pady=15, bg="green", fg="white")





ventana.mainloop()