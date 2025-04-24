from flask import Flask, render_template
from cliente_dao import ClienteDAO

servidor_flask = Flask(__name__)

titulo_app = 'Zona Fit (GYM)'

@servidor_flask.route('/') # url http://localhost:5000/
@servidor_flask.route('/index.html') # url http://localhost:5000/index.html
def inicio():
    servidor_flask.logger.debug('Inicio : /')

    # Recuperamos los clientes
    clientes_db = ClienteDAO.seleccionar_todos()
    return render_template("index.html", titulo = titulo_app, clientes = clientes_db)

if __name__ == '__main__': # __name__ = nombre de este archivo
    servidor_flask.run(debug=True)

