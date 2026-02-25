import sqlite3

#Le decimos que busque el id de la api
def select_comentarios(imdb_id):
    #Aquí se conectará con los datos guardados del browser
    conexion = sqlite3.connect('peliculas.db')
    #Llamamos al cursor para buscar
    cursor = conexion.cursor()
    #Traeme el nombre y el comentario que esten relacionados con la id
    cursor.execute("SELECT nombre, comentario FROM comentarios WHERE imdb_id = ?", (imdb_id,))
    #Aquí guardamos todos los datos que el cursor a encontrado
    resultado = cursor.fetchall()
    #cuando lo encuentres cierra la conexión
    conexion.close()
    #Devuelveme lo encontrado
    return resultado