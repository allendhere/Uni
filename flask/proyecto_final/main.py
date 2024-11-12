#importar flask
from flask import Flask, render_template

#declarar variable app
app=Flask(__name__)
#crear funcion de inicio y rutas

@app.route('/LOGIN')
def Login():
    return render_template('formularios/login.html')

@app.route('/')
def index():
    return render_template('pagina/principal.html')

@app.route('/ENLACE_1')
def Enlace_1():
    return render_template('pagina/pagina_1.html')

@app.route('/ENLACE_2')
def Enlace_2():
    return render_template('pagina/pagina_2.html')

@app.route('/APLICACION')
def Aplicacion():
    return render_template('formularios/aplicacion.html')


@app.route('/DBPERSONAJES')
def DBPersonajes():
    return render_template('pagina/DBPersonajes.html')



#fin cuerpo 
if __name__ == '__main__':
    app.run(debug=True)