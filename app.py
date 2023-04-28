from flask import Flask, render_template, abort, redirect, request

app = Flask(__name__)	

@app.route('/')
def inicio():
    return render_template("inicio.html")

@app.route('/juegos')
def articulos():
    return render_template("juegos.html")

@app.route('/listajuegos')
def acercade():
    return render_template("listajuegos.html")


app.run("0.0.0.0",5000,debug=True)