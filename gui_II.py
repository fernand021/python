import tkinter 
root = Tk()

miFrame = Frame(root, width=500, height=200)
miFrame.pack()

miNombre = StringVar()

cuadroNombre = Entry(miFrame, textvariable=miNombre)
cuadroNombre(row=0,column=1)
cuadroNombre.config(fg='red', justify='right')

cuadroApellido = Entry(miFrame)
cuadroApellido(row=1,column=1)

cuadroDireccion = Entry(miFrame)
cuadroDireccion(row=2,column=1)
cuadroDireccion.config(show='*')

textoComentario = Text(miFrame, width=16, height=5)
textoComentario.grid(row=4,column=1,padx=10, pady=10)

scrollVert = Scrollbar(miFrame,command = textoComentario.yview)
scrollVert.grid(row=4,column=2 , sticky='nsew ')

texto.comentario.config(yscrollcommand = scrollVert.set)

labelNombre = Label(miFrame, text='name')
labelNombre.grid(row=0,column=0, sticky='e',padx=10, pady=20)


labelApellido = Label(miFrame, text='name')
labelApellido.grid(row=1, column=0, sticky='e',padx=10, pady=20)


labelDireccion = Label(miFrame, text='name')
labelDireccion.grid(row=2,column=0, sticky='e',padx=10, pady=20)


comentariosLabel = Label(miFrame, text='comentarios:')
comentariosLabel.grid(row=4,column=0, sticky='e', padx=10, pady=10)


btnEnvio =Button(root,text='enviar', command=codigoBoton)
btnEnvio.pack()

def codigoBoton():
	miNombre.set('fernando')


root.mainloop()