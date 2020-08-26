


from tkinter import * 

root = Tk()

root.title('ejemplo')

playa = IntVar()
montaña = IntVar()
urbano = IntVar()

def opcionesViaje():
	opcionEscogida =''
	if(playa.get()==1):
		opcionEscogida+= ' playa '
	if(montaña.get()==2):
		opcionEscogida+= ' montaña '
	if(urbano.get()==3):
		opcionEscogida+= ' urbano '

	textoFinal.config(text=opcionEscogida)


foto = PhotoImage(file='avion.png')
label(root, image=foto).pack()


frame = frame(root)
frame.pack()

Label(frame, text='elige destinos ', width =40).pack()

checkbutton(root, text='playa', variable=playa, onvalue=1, offvalue=0, command=opcionesViaje).pack()
checkbutton(root, text='montaña', variable=montaña, onvalue=2, offvalue=0, command=opcionesViaje).pack()
checkbutton(root, text='urbano', variable=urbano, onvalue=3, offvalue=0, command=opcionesViaje).pack()

root.mainloop()