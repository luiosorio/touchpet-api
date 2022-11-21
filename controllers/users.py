from flask import request, jsonify
from firebaseConexion import database

def listaUsuarios():
    try:
        lista_usuarios = database.reference("/usuarios").get()
        if lista_usuarios:
            users = []
            for user in lista_usuarios:
                lista_usuarios[user]["identificacion"] = user
                lista_usuarios[user].pop("password")
                users.append(lista_usuarios[user])
            
            return jsonify(users), 200
        else:
            return jsonify(lista_usuarios), 200
    except Exception as e:
        print(e)
        return jsonify({'error': "Error en consulta de listado de usuarios"}), 500


def crearUsuario():
    try:
        if "identificacion" in request.json and "nombre" in request.json and "apellido" in request.json and "correo" in request.json and "password" in request.json:
            usuario_id = str(request.json["identificacion"])

            # verificamos si ya existia un usuario con la cedula ingresada
            usuario = database.reference(f"/usuarios/{usuario_id}").get()
            if usuario:
                return jsonify({'message': "Ya existe un usuario registrado en el sistema"}), 400
            else:
                # se crea el cliente en la base de datos
                database.reference("/usuarios").child(usuario_id).set(request.json)
                return jsonify({'message': "Creación realizada"}), 201
        else: 
            return jsonify({'message': "Data incompleta"}), 400
    except Exception as e:
        print(e)
        return jsonify( {'error': "Error en creacion del usuario"}), 500

def getUsuario(id):
    try:
        # se consulta el usuario en la base de datos
        usuario = database.reference(f"/usuarios/{str(id)}").get()
        if usuario:
            # eliminamos la contraseña para no mostrarla
            usuario.pop("password")
            return jsonify(usuario), 200
        else:
            return jsonify( {'error': "Usuario no encontrado"}), 404
    except Exception as e:
        print(e)
        return jsonify( {'error': "Error en consulta del usuario"}), 400

def deleteUsuario(id):
    try:
        # se consulta el usuario en la base de datos para verificar eliminacion
        usuario = database.reference(f"/usuarios/{str(id)}").get()
        if usuario:
            # se elimina el usuario en la base de datos
            database.reference(f"/usuarios/{str(id)}").delete()
            return jsonify({ "message": "usuario borrado con exito"}), 200
        else:
            return jsonify( {'error': "Usuario no encontrado"}), 404
    except Exception as e:
        print(e)
        return jsonify( {'error': "Error en eliminacion del usuario"}), 500

def updateUsuario(id):
    try:
        # consultamos el usuario en la base de datos antes de actualizar
        usuario_id = str(id)
        if usuario_id:
            usuario = database.reference(f"/usuarios/{usuario_id}").get()
            if usuario:
                # se actualiza el cliente en la base de datos con lo que llegue en el request json
                database.reference("/usuarios").child(usuario_id).update(request.json)
                return jsonify({'message': "Actualizacion realizada"}), 200
            else: 
                return jsonify({'message': "Usuario no encontrado para actualizar"}), 404
        else: 
            return jsonify({'message': "Debes enviar un id del usuario"}), 404

    except Exception as e:
        print(e)
        return jsonify( {'error': "Error en actualizacion del usuario"}), 500

def loginUsuario():
    try:
        if "identificacion" in request.json and "password" in request.json:
            usuario_id = str(request.json["identificacion"])
            password = str(request.json["password"])

            # verificamos si ya existia un usuario con la cedula ingresada
            usuario = database.reference(f"/usuarios/{usuario_id}").get()
            if usuario:
                # se verifica que la contraseña coincida
                if usuario["password"] == password:
                    return jsonify({'message': "Login Exitoso"}), 201
                else:
                    return jsonify({'message': "Datos incorrectos, intenta nuevamente"}), 400
            else:
                return jsonify({'message': "Contraseña incorrecta"}), 400
        else: 
            return jsonify({'message': "Data incompleta"}), 400
    except Exception as e:
        print(e)
        return jsonify( {'error': "Error en proceso de login"}), 500
