

# ================= EXPRESIONES REGULARES ===============
"""
    las expresiones regulares son una secuencia de caracteres que forman un patron de busqueda
    sirven : para el trabajo y procesamiento de texto
"""


import re

cadena = 'vamos a aprender expresiones regulares en python. python es un lenguaje de sintaxis sencillo'
textoBuscar = 'python'


textoEncontrado = re.search(textoBuscar, cadena)
print('empieza en la posicion ', textoEncontrado.start())
print('finaliza en la posicion ', textoEncontrado.end())
print(textoEncontrado.span())
print(textoBuscar, ' se repite ', len(re.findall(textoBuscar, cadena)))

"""
if re.search(textoBuscar,cadena) is not None:
    print('he encontrado el texto')
else:
    print('no he encontrado el texto')
"""

# print(re.search('aprender',cadena))

print('========================================')

listaNombres = ['ana gomez',
                'martin martin',
                'ximena alondra',
                'maria martin',
                'abigail alvizures',
                'abigail monterroso',
                'abigail esquivel']

for elemento in listaNombres:
    if re.findall('^abigail', elemento):
        print(elemento)

print('')

for elementos in listaNombres:
    if re.findall('martin$', elementos):
        print(elementos)

print('')

dominios = ['https//bytecode.com',
            'ftp//bytecode.es',
            'https//bytecoñde.com']

for e in dominios:
    if re.findall('[ñ]',e):
        print(e)


print('')
print('========================================')

listName = ['fernando',
            'ximena',
            'julissa',
            'abigail',
            'ma2',
            'ma1',
            'ma3']

for n in listName:
    if re.findall('[xa]', n):
        print(n)
    