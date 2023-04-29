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
#usando la función redirect()(para redireccionar a la página) y url_for().
#si la solicitud es GET, se ejecuta el else devolviendo el contenido HTML (/juegos.html)

@app.route('/juegos', methods = ['GET', 'POST'])
def juegos():
    if request.method == 'POST':
        nombre = request.form['nombre']
        return redirect(url_for('listajuegos', nombre = nombre))
    else:
        return render_template("juegos.html")


@app.route('/listajuegos')
def listajuegos():
    return render_template("listajuegos.html")


app.run("0.0.0.0",5000,debug=True)