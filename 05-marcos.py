from tkinter import *

ventana = Tk()
ventana.title("Marcos | Master en Python")
ventana.geometry("700x700")

#Marco
marco_padre = Frame(ventana,width=250,height=250)
# marco_padre.config(
#     bg="lightblue",
#     bd=5,
#     relief="solid"#raised
    
    
# )
marco_padre.pack(side=BOTTOM, fill=X, expand=YES, anchor=S)




marco = Frame(marco_padre,width=250,height=250)
marco.config(
    bg="red",
    bd=12,
    relief="solid"#raised
    
    
)
marco.pack(side=LEFT, anchor=SW)

marco.pack_propagate(False)
texto = Label(marco, text="Primer marco")
texto.config(
    bg="red",
    fg="white",
    font=("Arial", 20),
    height=10,
    width=10,
    bd=3,
    # relief=SOLID,
    # anchor=CENTER


)
texto.pack(anchor=CENTER,fill=Y,expand=YES)


marco = Frame(marco_padre,width=250,height=250)
marco.config(
    bg="green",
    bd=12,
    relief="solid"#raised
)
marco.pack(side=RIGHT, anchor=SE)



marco_padre = Frame(ventana,width=250,height=250)
# marco_padre.config(
#     bg="lightblue",
#     bd=5,
#     relief="solid"#raised
    
    
# )
marco_padre.pack(side=TOP, fill=X, expand=YES, anchor=N)


marco = Frame(marco_padre,width=250,height=250)
marco.config(
    bg="orange",
    bd=5,
    relief="raised"#raised
)
marco.pack(side=RIGHT)


marco = Frame(marco_padre,width=250,height=250)
marco.config(
    bg="purple",
    bd=5,
    relief="raised"#raised
)
marco.pack(side=LEFT)





ventana.mainloop()