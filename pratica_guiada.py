


from tkinter import *
from tkinter import messagebox

root = Tk()
# ======================= FUNCIONES ====================
def conexionBBDD():
    miConexion = sqlite3.connect('Usuarios')
    miCursor = miConexion.cursor()

    try:
        miCursor.execute('''
            CREATE TABLE DATOSUSUARIOS (
                ID INTEGER PRIMARY JEY AUTOINCREMENT,
                NOMBRE_USUARIO VARCHAR(50),
                PASSWORD VARCHAR(50),
                APELLIDO VARCHAR(10),
                DIRECCION VARCHAR(50),
                COMENTARIO VARCHAR(100)
                )
        ''')

        messagebox.showinfo('BBDD','BBDD creada con exito')
    except:
        messagebox.showwarning('Atencion','BBDD ya existe')

def salirApp():
    valor = messagebox.askquestion('salir','deseas salir de la aplicacion?')
    if valor =='yes':
        root.destroy()


def limpiarCampos():
    miNombre.set('')
    miId.set('')
    miApellido.set('')
    miDireccion.set('')
    miPass.set('')
    textoComentario.delete(1.0, END)



def crear():
    miConexion. = sqlite3.connect('Usuarios')
    miCursor = miConexion.cursor()

    datos =    miNombre.get(), miPass.get(), miApellido.get(),miDireccion.get(), textoComentario.get('1.0',END)
    """miCursor.execute('INSERT INTO DATOSUSUARIOS VALUES(NULL, "' + miNombre.get() +
        '","' + miPass.get() +
         '","' + miApellido.get() + 
         '","' + miDireccion.get()  +
         '","' + textoComentario.get('1.0', END) + '")')"""
    miCursor.execute('INSERT INTO DATOSUSUARIOS VALUES(NULL,?,?,?,?,?)',(datos))
    miConexion.commit()
    messagebox.showinfo('BBDD','registro con exito')


def leer():
    miConexion. = sqlite3.connect('Usuarios')
    miCursor = miConexion.cursor()

    miCursor.execute('SELECT * FROM DATOSUSUARIOS WHERE ID =' + miId.get())
    elUsuario = miCursor.fetchall()

    for usuario in elUsuario:
        miId.set(usuario[0])
        miNombre.set(usuario[1])
        miPass.set(usuario[2])
        miApellido.set(usuario[3])
        miDireccion.set(usuario[4])
        textoComentario.insert(1.0, usuario[5])

    miConexion.commit()

def Actualizar():
    miConexion. = sqlite3.connect('Usuarios')
    miCursor = miConexion.cursor()

    miCursor.execute('UPDATE DATOSUSUARIOS SET NOMBRE_USUARIO =  "' + miNombre.get() +
        '", PASSWORD = "' + miPass.get() +
         '",APELLIDO = "' + miApellido.get() + 
         '",DIRECCION = "' + miDireccion.get()  +
         '",COMENTARIOS"' + textoComentario.get('1.0', END) +
         '" WHERE ID = "' + miId.get())')

    miConexion.commit()
    messagebox.showinfo('BBDD','registro con actualizado exito')



def eliminar():
    miConexion. = sqlite3.connect('Usuarios')
    miCursor = miConexion.cursor()

    miCursor.execute('DELETE FROM DATOSUSUARIOS WHERE ID= ' + miId.get())

    miConexion.commit();
    messagebox.showinfo('BBDD', 'registro eliminado con exito')

# ===================== MENU ==========================
barraMenu = Menu(root)
root.config(menu=barraMenu, Width = 300, height=300)

bbddMenu = Menu(barraMenu, tearoff=0)
bbddMenu.add_command(Label='Conectar', command=conexionBBDD)
bbddMenu.add_command(Label='Exit',comman=salirApp)

borrarMenu = Menu(barraMenu, tearoff=0)
borrarMenu.add_command(Label='Borrar campos', command=limpiarCampos)

crudMenu = Menu(barraMenu, tearoff=0)
crudMenu.add_command(Label='Crear', command=crear)
crudMenu.add_command(Label='Actualizar', command = Actualizar)
crudMenu.add_command(Label='Leer', command = leer)
crudMenu.add_command(Label='Borrar', command=eliminar)

ayudaMenu = Menu(barraMenu, tearoff=0)
ayudaMenu.add_command(Label='Licencia')
ayudaMenu.add_command(Label='Acerca de')

barraMenu.add_cascade(Label='BBDD', menu=bbddMenu)
barraMenu.add_cascade(Label='Borrar', menu=borrarMenu)
barraMenu.add_cascade(Label='CRUD', menu=crudMenu)
barraMenu.add_cascade(Label='Ayuda', menu=ayudaMenu)



# ===================== CAMPOS ==========================
miFrame = Frame(root)
miFrame.pack()

miId=StringVar()
miNombre = StringVar()
miApellido = StringVar()
miPass = StringVar()
miDireccion = StringVar()


cuadroID = Entry(miFrame, textvariable=miId)
cuadroID.grid(row=0, column=1, padx = 10, pady=10)

cuadroNombre = Entry(miFrame, textvariable=miNombre)
cuadroNombre.grid(row=1, column=1, padx = 10, pady=10)

cuadroPassword = Entry(miFrame , textvariable=miPass)
cuadroPassword.grid(row=2, column=1, padx = 10, pady=10)
cuadroPassword.config(show=' * ')

cuadroApellido = Entry(miFrame , textvariable=miApellido)
cuadroApellido.grid(row=3, column=1, padx = 10, pady=10)

cuadroDireccion = Entry(miFrame , textvariable=miDireccion)
cuadroDireccion.grid(row=4, column=1, padx = 10, pady=10)

textoComentario = Text(miFrame, width=16, height=5)
textoComentario.grid(row=5, column=1, padx=10, pady=10)
scrollVert = Scrollbar(miFrame, command=textoComentario.yview)
scrollVert.grid(row=5, column=2, sticky='nsew')
textoComentario.config(yscrollcommand = scrollVert.set)

# ===================== LABEL ==========================
idLabel = Label(miFrame, text = 'ID')
idLabel.grid(row=0 ,column=0, sticky='e', padx = 10, pady=10)

nombreLabel = Label(miFrame, text = 'Nombre')
nombreLabel.grid(row=1 ,column=0, sticky='e', padx = 10, pady=10)

passwordLabel = Label(miFrame, text = 'Password')
passwordLabel.grid(row=2 ,column=0, sticky='e', padx = 10, pady=10)

apellidoLabel = Label(miFrame, text = 'Apellido')
apellidoLabel.grid(row=3 ,column=0, sticky='e', padx = 10, pady=10)

direccionLabel = Label(miFrame, text = 'Direccion')
direccionLabel.grid(row=4 ,column=0, sticky='e', padx = 10, pady=10)

ComentariosLabel = Label(miFrame, text = 'Comentarios')
ComentariosLabel.grid(row=5 ,column=0, sticky='e', padx = 10, pady=10)



# ===================== BTN ==========================
miFrame2 = Frame(root)
miFrame2.pack()

btnCrear = Button(miFrame2, text='Create', command=crear)
btnCrear.grid(row=0,column=0, sticky='e', padx=10, pady=10)

btnLeer = Button(miFrame2, text='Read',  command = leer)
btnLeer.grid(row=1,column=0, sticky='e', padx=10, pady=10)

btnActualizar = Button(miFrame2, text='Update', command = Actualizar)
btnActualizar.grid(row=2,column=0, sticky='e', padx=10, pady=10)

btnBorrar = Button(miFrame2, text='Delete',command=eliminar)
btnBorrar.grid(row=3,column=0, sticky='e', padx=10, pady=10)


root.mainloop()