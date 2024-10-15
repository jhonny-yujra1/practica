from flask import Flask, render_template, request

app=Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/quienes-somos')
def quienes_somos():
    return render_template('quienes_somos.html')

@app.route('/servicios')
def servicios():
    return render_template('servicios.html')

@app.route('/noticias')
def noticias():
    return render_template('noticias.html')

@app.route('/contacto', methods=['GET', 'POST'])
def contacto():
    if request.method == 'POST':
        # Aquí podrías manejar el envío del formulario
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        # Procesar los datos (guardar en DB, enviar un email, etc.)
        return render_template('contacto.html', success=True)
    return render_template('contacto.html')



if __name__ == "__main__":
    app.run(debug=True)