



from tkinter import * 
from tkinter import messagebox

root = Tk()

def infoAdicional():
    messagebox.showinfo('Procesador de  Fernando','Procesador de textos version 2020')

def aviso_licencia():
    messagebox.showwarning('Licencia','Producto bajo licencia GNU')

def salirApp():
    valor = messagebox.askquestion('Salir','¿deseas salir de la aplicacion?')
    if valor==='yes':
        root.destroy()

def cerrarDoc():
    valor = messagebox.askretrycancel('Reintentar','documento bloqueado')
    if valor===TRUE:
        root.destroy()


barraMenu = Menu(root)
root.config(menu=barraMenu, width=300, height=300)

archivoMenu = Menu(barraMenu, tearoff=0)
archivoMenu.add_command(Label='nuevo')
archivoMenu.add_command(Label='guardar')
archivoMenu.add_command(Label='guardar como')
archivoMenu.add_separator()
archivoMenu.add_command(Label='cerrar',command=cerrarDoc)
archivoMenu.add_command(Label='salir', command=salirApp)

archivoEdicion = Menu(barraMenu, tearoff=0)
archivoEdicion.add_command(Label='copy')
archivoEdicion.add_command(Label='save')
archivoEdicion.add_command(Label='cut')
archivoEdicion.add_separator()
archivoEdicion.add_command(Label='undo')
archivoEdicion.add_command(Label='replace')

archivoHerramientas = Menu(barraMenu, tearoff=0)

archivoAyuda = Menu(barraMenu, tearoff=0)
archivoAyuda.add_command(Label='licencia',command=aviso_licencia)
archivoAyuda.add_command(Label='acerca de', command=infoAdicional)

barraMenu.add_cascade(label='archivo', menu=archivoMenu)
barraMenu.add_cascade(label='Edicion', menu=archivoEdicion)
barraMenu.add_cascade(label='Herramientas', menu=archivoHerramientas)
barraMenu.add_cascade(label='Ayuda', menu=archivoAyuda)




root.mainloop()