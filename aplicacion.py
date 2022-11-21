from genericpath import exists
from flask import Flask, jsonify
from flask_cors import CORS
from firebaseConexion import database

from controllers.users import listaUsuarios, crearUsuario, getUsuario, deleteUsuario, updateUsuario, loginUsuario
from controllers.pets import listarMascotasUsuario, crearMascotaUsuario, getMascotaUsuario, deleteMascotaUsuario, updateMascotaUsuario, registrarAccionMascota, listarAccionesMascota


# instancia de la clase Flask
app = Flask(__name__)
CORS(app)

# rutas http para acceder desde un cliente http (Postman, Aplicacion Movil o Navegador)

# ruta de inicio (ejemplo)
@app.route('/api/')
def inicio():
   return jsonify({"message": "API de Touch Pet con Python, Flask y Firebase"}), 200

# endpoint para realizar el login a la plataforma
@app.route('/api/login', methods=['POST'])
def myLoginUsuario():
    return loginUsuario()

# endpoint para listar los usuarios de la plataforma
@app.route('/api/users')
def myListarUsuarios():
    return listaUsuarios()

# endpoint para crear usuarios en la plataforma
@app.route('/api/users', methods=['POST'])
def myCrearUsuario():
    return crearUsuario();

# endpoint para obtener detalles de usuarios en la plataforma
@app.route('/api/users/<id>')
def myGetUsuario(id):
    return getUsuario(id)

# endpoint para eliminar usuarios en la plataforma
@app.route('/api/users/<id>', methods=['DELETE'])
def myDeleteUsuario(id):
    return deleteUsuario(id)

# endpoint para actualizar la informacion de usuarios en la plataforma
@app.route('/api/users/<id>', methods=['PUT'])
def myUpdateUsuario(id):
    return updateUsuario(id)

# endpoint para listar las mascotas de un usuario en la plataforma
@app.route('/api/users/<userId>/pets')
def myListarMascotasUsuario(userId):
    return listarMascotasUsuario(userId)

# endpoint para crear mascotas de un usuario en la plataforma
@app.route('/api/users/<userId>/pets', methods=['POST'])
def myCrearMascotaUsuario(userId):
    return crearMascotaUsuario(userId)

# endpoint para obtener la informacion de una mascota de un usuario en la plataforma
@app.route('/api/users/<userId>/pets/<id>')
def myGetMascotaUsuario(userId, id):
    return getMascotaUsuario(userId, id)

# endpoint para eliminar mascotas de un usuario en la plataforma
@app.route('/api/users/<userId>/pets/<id>', methods=['DELETE'])
def myDeleteMascotaUsuario(userId, id):
    return deleteMascotaUsuario(userId, id)

# endpoint para actualizar la informacion de una mascota de un usuario en la plataforma
@app.route('/api/users/<userId>/pets/<id>', methods=['PUT'])
def myUpdateMascotaUsuario(userId, id):
    return updateMascotaUsuario(userId, id)

# endpoint para registrar una accion pulsada por la mascota
@app.route('/api/users/<userId>/pets/<id>/acciones', methods=['POST'])
def myRegistrarAccionMascota(userId, id):
    return registrarAccionMascota(userId, id)

# endpoint para listar las acciones de una mascota
@app.route('/api/users/<userId>/pets/<id>/acciones', methods=['GET'])
def myListarAccionesMascota(userId, id):
    return listarAccionesMascota(userId, id)


# función principal, activa el servidor como aplicación web
# y un seguimiento de mensajes con el debug en True
if __name__ == '__main__':
   app.run(debug=True)