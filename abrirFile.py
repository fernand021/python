


from tkinter import * 
from tkinter import filedialog

root = Tk()

def abreFichero():
    """
    initialdir = en que directorio queremos que se abra la carpeta
    filetypes = que archivos queremos permiter
    """
    fichero = filedialog.askopenfile(title='abrir', initialdir='c:', filetypes=(('ficheros de excel','*xls'), ('ficheros de texto','*txt'), ('todos los ficheros','*.*')))
    print(fichero)


Button(root, text='abrir fichero', command=abreFichero).pack()



root.mainloop()