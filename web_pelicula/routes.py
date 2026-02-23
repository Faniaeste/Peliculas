from web_pelicula import app
from flask import render_template,request
#Llamo a las dos funciones par poderlas utilizar en las rutas
from .services.omdb_service import obtener_peliculas,obtener_detalles_pelicula

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

