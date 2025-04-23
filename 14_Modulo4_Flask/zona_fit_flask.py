from flask import Flask, render_template

servidor_flask = Flask(__name__)

titulo_app = 'Zona Fit (GYM)'

@servidor_flask.route('/') # url http://localhost:5000/
@servidor_flask.route('/index.html') # url http://localhost:5000/index.html
def inicio():
    servidor_flask.logger.debug('Inicio : /')
    return render_template("index.html", titulo = titulo_app)

if __name__ == '__main__': # __name__ = nombre de este archivo
    servidor_flask.run(debug=True)

