

import sqlite3

miConexion = sqlite3.connect('GestionProductos1')
miCursor = miConexion.cursor()

# lectura de registros
miCursor.execute('SELECT  * FROM PRODUCTOS WHERE SECCION = "CONFECCION"')
# actualizar datos
miCursor.execute(
    'UPDATE PRODUCTOS SET PRECIO = 35 WHERE NOMBRE_ARTICULO ="pelota"')
miCursor.execute('DELETE FROM PRODUCTOS WHERE ID=5')  # elimina datos


productos = miCursor.fetchall()

print(productos)

miCursor.commit()
miConexion.close()
