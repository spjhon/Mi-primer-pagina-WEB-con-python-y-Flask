# Desde este archivo va a arrancar la aplicacion

from flask import Flask, render_template # Primero lo importamos, con render template se renderiza el html y es una funcion de FLASK

app = Flask(__name__) #Esto indica que este es el archivo que va a arrancar mi aplicacion y vamos a guardalo en una constante
                # LLamada app, con esta variable se van a poder hacer cosas como rutas del servidor, URL  y demas.
# Luego hay que crear las rutas, para ello utilizamos un decorador

@app.route('/') #De esta forma se le esta diciendo a python que esta es la pagina princiapl
# Se esta creando una ruta para la pagina principal.

#Ahora cuando el usuario entre a la pagina principal pues se va a tener que retornar algo
#En ese caso utilizaremos una funcion 
def home(): # Esta funcion retorna algo al navegador
    return render_template('home.html')


# Ahora vamos a crear otra ruta en este caso es para el about
# En este caso estamos enviando texto, pero lo ideal es que se envie datos HTML, Y se guardan en TEMPLATES
@app.route('/about')
def about():
    return render_template('about.html')


# Ahora hacemos una validacion para comprobar si estamos en el archivo principal
if __name__ == '__main__':
    app.run(debug=True) # con este metodo nos permite ejecutar la aplicacion, OJO EL DEBUG ES MODO PRUEBA
    