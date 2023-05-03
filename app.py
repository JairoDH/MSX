from flask import Flask, render_template, abort, redirect, request
import json

app = Flask(__name__)	

#abrir la información del json
with open ('MSX.json') as msx:
    datos = json.load(msx)

#página principal 
@app.route('/')
def inicio():
    return render_template("inicio.html")

#definición de función de vista (GET, cuando se accede a la página y POST, el usuario envía información por el formulario)
#si el usuario introduce información se extrae el valor del campo entrada nombre y redirige a la página de resultados de búsqueda
#usando la función render_template()(para redireccionar a la página) y url_for().
#si la solicitud es GET, se ejecuta el else devolviendo el contenido HTML (/juegos.html)

@app.route('/juegos', methods = ["GET", "POST"])
def juegos():
    if request.method == 'POST':
        nombre = request.form.get["nombre"]
        return render_template("listajuegos.html", nombre = nombre)
    else:
        return render_template("juegos.html", datos = datos)

#funcion de vista POST (introducido anteriormente por el usuario), se extrae el valor de entrada nombre del formulario
#y se realiza la búsqueda en la lista de la variable datos(variable donde esta el json.MSX)
#cuyo nombre comience por el valor del campo nombre(.startswith()) y lo añade a la lista resultados
#devuelve (return) la plantilla HTML(listajuegos) y pasa la lista resultados.

@app.route('/listajuegos', methods =["POST"])
def listajuegos():
    nombre = str(request.form['nombre'])
    resultado = []
    for juego in datos:
        if str(juego['nombre']).lower().startswith(str(nombre).lower()):
            resultado.append(juego)
    else:
        return render_template("listajuegos.html",resultado = resultado)
    



app.run("0.0.0.0",5000,debug=True)