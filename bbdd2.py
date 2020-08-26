



import sqlite3

miConexion = sqlite3.connect('GestionProductos')
miCursor = miConexion.cursor()

miCursor.execute('''
    CREATE TABLE PRODUCTOS(
        CODIGO_ARTICULO VARCHAR(4) PRIMARY KEY AUTOINCREMENT,
        NOMBRE_ARTICULO VARCHAR(50) UNIQUE,
        PRECIO INTEGER,
        SECCION VARCHAR(20)
    )
''')




productos = [
    ('AR01','PELOTA',20,'JUGUETERIA'),
    ('AR02','PANTALON',20,'ROPA'),
    ('AR03','MARTILLO',20,'HERRAMIENTAS'),
]
miCursor.executemany('INSERT INTO PRODUCTOS VALUES (?,?,?,?)', productos)

miCursor.commit()

miConexion.close()