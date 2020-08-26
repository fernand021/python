



from tkinter import *


raiz = Tk()
raiz.title(' title ')
# raiz.resizable(True,False)
# raiz.iconbitmap('gato.ico')
raiz.geometry('700x500')
raiz.config(bg ='green')

miFrame = Frame()
miFrame.pack(side = 'bottom' , anchor=n)
miFrame.pack(fill='x')
miFrame.config(bg=yellow)
miFrame.config(width='650', height='350')
miFrame.config(bd=35)
miFrame.config(relief='groove')
miFrame.config(cursor='pirate')

raiz.mainloop() 