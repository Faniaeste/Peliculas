import sqlite3

#Le decimos que busque el id de la api
def select_comentarios(imdb_id):
    #Aquí se conectará con los datos guardados del browser
    conexion = sqlite3.connect('peliculas.db')
    #Llamamos al cursor para buscar
    cursor = conexion.cursor()
    #Traeme el nombre y el comentario que esten relacionados con la id
    cursor.execute("SELECT nombre, comentario, strftime('%d/%m/%Y %H:%M',fecha) FROM comentarios WHERE imdb_id = ?", (imdb_id,))
    #Aquí guardamos todos los datos que el cursor a encontrado
    resultado = cursor.fetchall()
    #cuando lo encuentres cierra la conexión
    conexion.close()
    #Devuelveme lo encontrado
    return resultado

#Función para guardar un nuevo comentario
def insertar_comentario(imdb_id, nombre, comentario):
    conexion = sqlite3.connect('peliculas.db')
    cursor = conexion.cursor()
    #Aquí le digo que guarde y donde
    #Los??? son un metodo de seguridad 
    #Las """ son para que no sea tan largo el codigo y hacer varias lineas
    cursor.execute('''
        INSERT INTO comentarios (imdb_id, nombre, comentario)
        VALUES (?, ?, ? )
    ''', (imdb_id, nombre, comentario))
    
    #commit guarda en la tabla lo comentado    
    conexion.commit()
    #Cierro la conexión para que no se pierdan los datos guardados
    conexion.close()