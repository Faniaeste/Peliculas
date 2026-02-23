import requests
from config import SECRET_KEY

URL_BASE = "http://www.omdbapi.com/"

#Pongo el año en None porque no es obligatorio y así no se rompe la web sino se introduce
#Esta función busca la lista de películas
def obtener_peliculas(titulo, anno=None):
    params = {
        'apikey': SECRET_KEY,
        's': titulo,
        'y': anno
    }
    try:
        response = requests.get(URL_BASE, params=params)
        #devuelve los datos como vienen de la api
        return response.json()
    except Exception:
        return{"Response":"False","Error":"Error de conexión"}

#Esta función busca una sola película por el id   
def obtener_detalles_pelicula(id):
    params = {
        'apikey': SECRET_KEY,
        'i': id,
    }
    try:
        response = requests.get(URL_BASE,params=params)
        return response.json()
    except Exception:
        return {"Response": "False", "Error": "No se pudo obtener el detalle"}