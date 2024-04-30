from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def inicio():
	return render_template("inicio.html")

@app.route('/registro_inst')
def registro_inst():
	return render_template("registro_inst.html")

@app.route('/registrar')
def registrar():
	return render_template("registrar.html")

@app.route('/registros')
def registros():
	return render_template("registros.html")

@app.route('/sobre_nosotros')
def sobre_nosotros():
	return render_template("sobre_nosotros.html")

@app.route('/terminos')
def terminos():
	return render_template("terminos.html")

@app.route('/contacto')
def contacto():
	return render_template("contacto.html")

if __name__ == '__main__':
	app.run(debug=True)