"""
Crear un programa que tenga:
- Una ventana
- Tamaño fijo
- No redimensionable
- Diferetes pantallas
- Formulario de añadir productos
- Guardar datos temporalmente
- Mostrar datos listados en la pantalla home
- Opcion de salir
"""


from tkinter import *
from tkinter import ttk

#Definir ventana
ventana = Tk()

#Cargar ventana
ventana.geometry("450x450")
ventana.minsize(500,500)
ventana.title("Proeycto Tkinter")
ventana.resizable(0,0)



# Pantallas
def home():
    # Mostrar pantalla
    home_label.config(
        fg="white",
        bg="black",
        font=("Arial", 30),
        padx=180,
        pady=20
    )
    home_label.grid(row=0, column=0)
    products_box.grid(row=2)

    #Listar productos
    # for product in products:
    #     if len(product) == 3:
    #         product.append("added")
    #         Label(products_box, text=product[0]).grid()
    #         Label(products_box, text=product[1]).grid()
    #         Label(products_box, text=product[2]).grid()
    #         Label(products_box, text="------------------").grid()



    for product in products:
        if len(product) == 3:
            product.append("added")
            products_box.insert('',0,text=product[0],values=(product[1]))

    #Ocultar otras pantallas
    add_label.grid_remove()
    add_frame.grid_remove()
    info_label.grid_remove()
    data_label.grid_remove()



def add():
    #Encabezado
    add_label.config(
        fg="white",
        bg="black",
        font=("Arial", 30),
        padx=60,
        pady=20
    )
    add_label.grid(row=0, column=0, columnspan=10)

     #Campos del formulario
    add_frame.grid(row=1)
    add_name_label.grid(row=1, column=0, padx=5, pady=5, sticky=E)
    add_name_entry.grid(row=1, column=1, padx=5, pady=5, sticky=W)

    add_precio_label.grid(row=2, column=0, padx=5, pady=5, sticky=E)
    add_precio_entry.grid(row=2, column=1, padx=5, pady=5, sticky=W)

    add_desc_label.grid(row=3, column=0, padx=5, pady=5, sticky=NW)
    add_desc_entry.grid(row=3, column=1, padx=5, pady=5, sticky=W)
    add_desc_entry.config(
        width=30,
        height=5,
        font=("Consolas", 12),
        padx=15,
        pady=15
    )


    add_separator.grid(row=4)


    boton.grid(row=5, column=1, sticky=E)
    boton.config(
        padx=15,
        pady=5,
        bg = "green",
        fg = "black"
    )

     #Ocultar otras pantallas
    home_label.grid_remove()
    products_box.grid_remove()
    info_label.grid_remove()
    data_label.grid_remove()






def info():
    info_label.config(
        fg="white",
        bg="black",
        font=("Arial", 30),
        padx=130,
        pady=20
    )
    info_label.grid(row=0, column=0)
    data_label.grid(row=1, column=0)

    home_label.grid_remove()
    products_box.grid_remove()
    add_frame.grid_remove()
    add_label.grid_remove()
    data_label.grid_remove()



def add_product():
    products.append([
        name_data.get(),
        price_data.get(),
        add_desc_entry.get("1.0", "end-1c")
    ])

    name_data.set("")
    price_data.set("")
    add_desc_entry.delete("1.0", END)
    
    home()




# Variables importantes
products = []
name_data = StringVar()
price_data  = StringVar()


# Definir campos de pantalla HOME
home_label = Label(ventana, text="Inicio")
# products_box = Frame(ventana, width=250)

# Label(products_box).grid(row=0)
Label(ventana).grid(row=1)
products_box = ttk.Treeview(height=12, columns=2)
products_box.grid(row=1, column=0, columnspan=2)
products_box.heading("#0",text="Producto",ancho=W)
products_box.heading("#1",text="Precio",ancho=W)

# Definir campos de pantalla ADD
add_label = Label(ventana, text="Añadir un producto")


# Campos del formulario
add_frame = Frame(ventana)

add_name_label = Label(add_frame, text="Nombre: ")
add_name_entry = Entry(add_frame, textvariable=name_data)
add_precio_label = Label(add_frame, text="Precio: ")
add_precio_entry = Entry(add_frame, textvariable=price_data)
add_desc_label = Label(add_frame, text="Descripción: ")
add_desc_entry = Text(add_frame)

add_separator = Label(add_frame)

boton = Button(add_frame, text= "Guardar", command=add_product)


# Definir campos de pantalla INFO
info_label = Label(ventana, text="Información")
data_label = Label(ventana, text="Creado por Aarón Huerta - 2022")


# Cargar la pantalla de inicio
home()


# Definir el menu
menu_superior = Menu(ventana)
menu_superior.add_command(label="Inicio", command=home)
menu_superior.add_command(label="Añadir", command=add)
menu_superior.add_command(label="Información", command=info)
menu_superior.add_command(label="Salir", command=ventana.quit)



# Cargar el menú
ventana.config(menu=menu_superior)


# Cargar ventana
ventana.mainloop()


