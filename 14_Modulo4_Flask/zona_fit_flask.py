from flask import Flask, render_template, redirect, url_for
from cliente_dao import ClienteDAO
from cliente import Cliente
from cliente_form import ClienteForm

servidor_flask = Flask(__name__)

servidor_flask.config['SECRET_KEY'] = 'llave_secreta_432'

titulo_app = 'Zona Fit (GYM)'

@servidor_flask.route('/') # url http://localhost:5000/
@servidor_flask.route('/index.html') # url http://localhost:5000/index.html
def inicio():
    servidor_flask.logger.debug('Inicio : /')

    # Recuperamos los clientes
    clientes_db = ClienteDAO.seleccionar_todos()
    # Objeto ClienteForm vacio
    cliente = Cliente()
    cliente_form = ClienteForm(obj=cliente)
    return render_template("index.html", titulo = titulo_app, clientes = clientes_db, cl_form = cliente_form)

@servidor_flask.route('/guardar', methods=['POST'])
def guardar_cliente():
    # Creamos los objetos de cliente
    cliente = Cliente()
    cliente_form = ClienteForm(obj=cliente)
    if cliente_form.validate_on_submit():
        # LLenamos el objeto cliente
        cliente_form.populate_obj(cliente)

        if not cliente.id:
            # Guardamos el nuevo cliente
            ClienteDAO.crear(cliente)
        else:
            # Guardamos el cliente actualizado
            ClienteDAO.actualizar(cliente)

        # Redireccionar al inicio
        return redirect(url_for('inicio'))

@servidor_flask.route('/eliminar/<int:id_cl>')
def eliminar_cliente(id_cl):
    cliente = Cliente(p_id=id_cl)
    ClienteDAO.eliminar_uno(cliente)
    return redirect(url_for('inicio'))

@servidor_flask.route('/limpiar')
def limpiar_formulario():
    return redirect(url_for('inicio'))

@servidor_flask.route('/editar/<int:id_cl>')
def editar_cliente(id_cl):
    cliente = ClienteDAO.seleccionar_uno_con_id(id_cl)
    cliente_form = ClienteForm(obj=cliente)

    # Recuperamos los clientes (para el listado)
    clientes_db = ClienteDAO.seleccionar_todos()

    return render_template('index.html', titulo = titulo_app, cl_form = cliente_form, clientes = clientes_db)




if __name__ == '__main__': # __name__ = nombre de este archivo
    servidor_flask.run(debug=True)

