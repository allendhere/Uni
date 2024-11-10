#importar flask
from flask import Flask, render_template

#declarar variable app
app=Flask(__name__)
#crear funcion de inicio y rutas


@app.route('/')
def index():
    return render_template('pagina/principal.html')

@app.route('/ENLACE_1')
def Enlace_1():
    return render_template('pagina/pagina_1.html')

@app.route('/ENLACE_2')
def Enlace_2():
    return render_template('pagina/pagina_2.html')

@app.route('/LOGIN')
def Login():
    return render_template('formularios/login.html')

@app.route('/APLICACION')
def Aplicacion():
    return render_template('formularios/aplicacion.html')

#ruta reporte
@app.route('/REPORTE')
def Reporte():
    return render_template('formularios/reporte.html')

#ruta modificar
@app.route('/MODIFICAR')
def Modificar():
    return render_template('formularios/modificar.html')

#ruta agregar
@app.route('/AGREGAR')
def Agregar():
    return render_template('formularios/agregar.html')



#fin cuerpo 
if __name__ == '__main__':
    app.run(debug=True)