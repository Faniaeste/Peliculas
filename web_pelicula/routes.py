from web_pelicula import app
from flask import render_template,request
from config import SECRET_KEY
import requests

@app.route("/")
def index():
    return render_template("index.html", dataForm={}, button="Buscar película")

@app.route("/buscar")
def buscar():
    titulo = request.values.get('t')
    anno = request.values.get('y')
    #Aquí guardo lo escrito por el cliente
    datos = {'titulo':titulo, 'anno':anno}
    url = f"http://www.omdbapi.com/?apikey={SECRET_KEY}&t={titulo}&y={anno}"

    respuesta = requests.get(url)
    pelicula = respuesta.json()

    if pelicula.get('Response') == 'True':
        return render_template("results.html", dataForm=pelicula, button="Buscar película")
    else:
        #Aquí en dataform dejo los datos ya escritos
        return render_template("index.html", dataForm=datos, error="No encontramos la película", button="Buscar película")
