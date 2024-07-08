from flask import Flask
from flask import Flask, render_template

app = Flask(__name__)

# Ruta para la página de inicio
@app.route('/')
def index():
    return render_template('index.html')

# Ruta para la página de contacto
@app.route('/contacto')
def contacto():
    return render_template('contacto.html')

# Ruta para la página de registro de estudiantes
@app.route('/registrar')
def registrar():
    return render_template('registrar.html')

# Ruta para la página de registro institucional
@app.route('/registro_inst')
def registro_inst():
    return render_template('registro_inst.html')

# Ruta para la página de términos y condiciones
@app.route('/terminos')
def terminos():
    return render_template('terminos.html')

# Ruta para la página sobre nosotros
@app.route('/sobre_nosotros')
def sobre_nosotros():
    return render_template('sobre_nosotros.html')

# Ruta para la página principal (layout)
@app.route('/main')
def main():
    return render_template('main.html')

if __name__ == '__main__':
    app.run(debug=True)
