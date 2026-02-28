from web_pelicula import app
from flask import render_template,request,redirect,url_for
#Llamo a las dos funciones par poderlas utilizar en las rutas
from web_pelicula.services.omdb_service import obtener_peliculas,obtener_detalles_pelicula
from web_pelicula import models

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
    #Busca los detalles de la pelicula llamando a la función
    detalles = obtener_detalles_pelicula(id)
    #Busca los comentarios relacionados con ese id llamando a la función
    comentarios = models.select_comentarios(id)
    #Lo muestro en la pantalla
    return render_template("results.html", dataForm=detalles, comentarios=comentarios)

#Aquí guardamos los datos y comentarios de los clientes cogidos en results.html
@app.route("/guardar_comentario/<imdb_id>", methods=['POST'])
def guardar_comentario(imdb_id):
    #Sacamos los datos del formulario (request.form)
    nombre = request.form.get('nombre')
    comentario = request.form.get('comentario')

    #Usamos la función que acabamos de crear en models
    models.insertar_comentario(imdb_id, nombre, comentario)

    #Volvemos a la página del detalle de la película
    return redirect(url_for('detalle', id=imdb_id))

