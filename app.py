from flask import Flask, render_template, abort, request
import json

app = Flask(__name__)	

#abrir la información del json
with open ('MSX.json') as msx:
    datos = json.load(msx)

#página principal 
@app.route('/')
def inicio():
    return render_template("inicio.html")

#juegos(): Esta función es la vista de la página "juegos". Si la solicitud es "GET", devuelve la plantilla HTML "juegos.html" y pasa la variable datos que contiene los datos de los juegos. 
#Si la solicitud es "POST", extrae el valor del campo "nombre" del formulario y redirige a la página "listajuegos.html".

@app.route('/juegos', methods = ["GET", "POST"])
def juegos():
    if request.method == 'POST':
        nombre = request.form.get("nombre")
        return render_template("listajuegos.html", nombre = nombre)
    else:
        return render_template("juegos.html", datos = datos)

#listajuegos(): Es la función que se encarga de procesar la solicitud POST del formulario de búsqueda. 
#Extrae el valor del campo "nombre" del formulario, busca los juegos cuyo nombre comienza con el valor del campo "nombre"
# y los añade a una lista resultado. Devuelve la plantilla HTML "listajuegos.html" y pasa la variable resultado.

@app.route('/listajuegos', methods =["POST"])
def listajuegos():
    nombre = str(request.form['nombre'])
    resultado = []
    for juego in datos:
        if str(juego['nombre']).lower().startswith(str(nombre).lower()):
            resultado.append(juego)
    else:
        return render_template("listajuegos.html",resultado = resultado)
#detallesjuegos(): Es la función que se encarga de renderizar la plantilla HTML de la página de detalles de un juego. 
#El identificador del juego se pasa como parámetro de ruta y se utiliza la función int() para convertirlo en un entero. 
#La función busca el juego con ese identificador en la lista datos y devuelve la plantilla HTML "juego.html" y pasa la variable juego.

@app.route('/juego/<int:identificador>', methods =["GET"])
def detallesjuegos(identificador):
    for juego in datos:
        if juego['id'] == identificador:
            return render_template('juego.html', juego=juego)
    abort(404)
      
app.run("0.0.0.0",5001,debug=True)