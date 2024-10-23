#importar flask
from flask import Flask, render_template

#declarar variable app
app=Flask(__name__)
#crear funcion de inicio y rutas


@app.route('/')
def index():
    return render_template('principal.html')

@app.route('/ENLACE_1')
def Enlace_1():
    return render_template('pagina_1.html')

@app.route('/ENLACE_2')
def Enlace_2():
    return render_template('pagina_2.html')


#fin cuerpo 
if __name__ == '__main__':
    app.run(debug=True)