

from tkinter import *


root = Tk()
miFrame = Frame(root, width=500, height=400)

miFrame.pack()
miImagen =PhotoImage(file='ruta')

miLabel = label(miFrame, text = 'hola alumnos de python' , font=('comic sans ms')).place(x=100,y=200)
miLabel.pack()

root.mainloop()