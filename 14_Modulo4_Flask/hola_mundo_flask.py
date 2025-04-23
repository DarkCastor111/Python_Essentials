from flask import Flask

servidor_flask = Flask(__name__)

@servidor_flask.route('/') # url http://localhost:5000/
def inicio():
    servidor_flask.logger.debug('Path de inicio : /')
    return '<p>Hola Mundo<p>'

if __name__ == '__main__': # __name__ = nombre de este archivo
    servidor_flask.run(debug=True)

