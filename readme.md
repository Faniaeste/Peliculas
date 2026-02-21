# Aplicación web con Flask y Sqlite

programa hecho en python con el framework flask y sqlite

# Instalación 

-Crear un entorno en python, activarlo y ejecutarlo 

'''
pip install -r requerimentos.txt
'''

la libreria utlizzada es https://flask.palletsprojects.com

# Ejecución del programa

-Inicializar parametros para el servidor de Flask en windows

'''
set FLASK_APP=main.py
'''
-comando para ejecutar el servidor

'''
flask --app main run
'''
-comando para ejecutar el servidor en otro pueto diferente al que viene por defecto que es el de 5000

'''
flask --app main run -o 5002

-comando para activar el servidor de flask en modo debug, no para el servidor para ver los cambios

'''
flask --app main --debug run
'''