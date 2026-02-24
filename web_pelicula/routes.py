from web_pelicula import app
from flask import render_template,request,redirect,url_for
#Llamo a las dos funciones par poderlas utilizar en las rutas
from .services.omdb_service import obtener_peliculas,obtener_detalles_pelicula
#Esto crea la conexión entre la base de datos y la web
import sqlite3

#Pantalla principal
@app.route("/")
def index():
    return render_template("index.html", dataForm={}, button="Buscar película")

@app.route("/buscar", methods=['GET'])
def buscar():
    titulo = request.values.get('t')
    anno = request.values.get('y')
    
    datos = obtener_peliculas(titulo,anno)
    
    if datos.get('Response') == 'True':
        #Al pedir Search pido que traiga todos los detalles
        return render_template("index.html", lista_peliculas=datos.get('Search'), dataForm={'titulo': titulo, 'anno':anno}, button="Buscar película")
    else:
        #Aquí en dataform dejo los datos ya escritos
        return render_template("index.html", dataForm={'titulo': titulo, 'anno': anno}, error="No encontramos la película", button="Buscar película")

# Aquí ponemos que busque el id de la pelicula para mostrar todos los que se llamen así,
# y los detalles que tenga, con el botón.
@app.route("/detalle/<id>")
def detalle(id):
    detalles = obtener_detalles_pelicula(id)
    return render_template("results.html", dataForm=detalles)

#Aquí guardamos los datos y comentarios de los clientes cogidos en results.html
@app.route("/guardar_comentario/<id>", methods=['POST'])
def guardar_comentario(id):
    nombre = request.form.get('nombre')
    comentario = request.form.get('comentario')

    conexion = sqlite3.connect('peliculas.db')
    #Aquí llamo a la funcion
    cursor = conexion.cursor()
    #Aquí le digo que guarde y donde
    #Los??? son un metodo de seguridad
    cursor.execute('''
        INSERT INTO comentarios (id, nombre, comentario,)
        VALUES (?, ?, ?, )''', (id, nombre, comentario,))
    
    #commit guarda en la tabla lo comentado    
    conexion.commit()
    #Cierro la conexión para que no se pierdan los datos guardados
    conexion.close()

    #url_for busca la dirección results  y le dice que busque ese id
    return redirect(url_for('guardar_comentario', id=id))

