



from tkinter import * 
root = Tk()


varOpcion = IntVar()


def imprimit():
	#print(varOpcion.get())
	if varOpcion.get()==1:
		etiqueta.config(text='has elegido masculino')
	else:
		etiqueta.config(text='has elegido femenino')

Label(root,text ='genero : ').pack()

Radiobutton(root, text='masculino', variable = varOpcion, value=1, command=imprimit).pack()
Radiobutton(root, text='femenino',  variable = varOpcion, value=2, command=imprimit).pack()

etiqueta  = Label(root)
etiqueta.pack()


root.mainloop()