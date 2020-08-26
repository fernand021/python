




"""
SQLite
    ventajas: 
        ocupa muy poco espacio
"""

import sqlite3

miConexion = sqlite3.connect('primeraBase')
miCursor = miConexion.cursor()

#miCursor.execute('CREATE TABLE PRODUCTOS(nombre articulo VARCHAR(50), precio INTEGER, seccion VARCHAR(20))')
#miCursor.execute('INSERT INTO PRODUCTOS VALUES ("BALON",15, "DEPORTES")')

variosProductos[
    ('camiseta ',10,'deportes'),
    ('jarron ',90,'ceramica'),
    ('carro ',20,'jugueteria')
]

miCursor.executemany('INSERT INTO PRODUCTOS VALUES (?,?,?)')


miCursor.commit()

miConexion.close()
