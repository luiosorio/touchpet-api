from tkinter import commondialog
from flask import request, jsonify
from firebaseConexion import database
from datetime import datetime

def listarMascotasUsuario(userId):
    try:
        usuario = database.reference(f"/usuarios/{str(userId)}").get()
        if usuario:
            lista_mascotas = database.reference(f"/usuarios/{str(userId)}/mascotas").get()
            if lista_mascotas:
                pets = []
                for petId in lista_mascotas:
                    lista_mascotas[petId]["nombre"] = petId
                    if ("acciones" in lista_mascotas[petId]):
                        lista_mascotas[petId]["acciones"] = len(lista_mascotas[petId]["acciones"])
                    else:
                        lista_mascotas[petId]["acciones"] = 0
                    pets.append(lista_mascotas[petId])
                
                return jsonify(pets), 200
            else:
                return jsonify(lista_mascotas), 200
        else:
            return jsonify({'error': "Usuario no encontrado"}), 404
    except Exception as e:
        print(e)
        return jsonify({'error': "Error en consulta de listado de mascotas del usuario"}), 500


def crearMascotaUsuario(userId):
    try:
        usuario = database.reference(f"/usuarios/{str(userId)}").get()
        if usuario:

            if "nombre" in request.json and "raza" in request.json and "personalidad" in request.json and "kgs" in request.json and "tamanio" in request.json and "fechaCumpleanios" in request.json:
                
                mascota_id = str(request.json["nombre"])

                # verificamos si ya existia una mascota del usuario con el nombre ingresado
                mascota = database.reference(f"/usuarios/{userId}/mascotas/{mascota_id}").get()
                if mascota:
                    return jsonify({'message': "Ya creaste una mascota con el mismo nombre"}), 400
                else:
                    # se crea el la mascota para el cliente en la base de datos
                    nuevaMascota = database.reference(f"/usuarios/{userId}/mascotas").child(mascota_id).set(request.json)
                    return jsonify(request.json), 201
            else: 
                return jsonify({'message': "Data incompleta"}), 400
        else:
            return jsonify({'error': "Usuario no encontrado"}), 404
    except Exception as e:
        print(e)
        return jsonify( {'error': "Error en creacion del usuario"}), 500

def getMascotaUsuario(userId, id):
    try:
        # se consulta la mascota en la base de datos
        mascota = database.reference(f"/usuarios/{userId}/mascotas/{id}").get()
        if mascota:
            return jsonify(mascota), 200
        else:
            return jsonify( {'error': "Mascota no encontrada"}), 404
    except Exception as e:
        print(e)
        return jsonify( {'error': "Error en consulta de la mascota"}), 400

def deleteMascotaUsuario(userId, id):
    try:
        # se consulta la mascota en la base de datos para verificar eliminacion
        mascota = database.reference(f"/usuarios/{userId}/mascotas/{id}").get()
        if mascota:
            # se elimina la mascota en la base de datos
            database.reference(f"/usuarios/{userId}/mascotas/{id}").delete()
            return jsonify({ "message": "Mascota borrada con exito"}), 200
        else:
            return jsonify( {'error': "Mascota no encontrada"}), 404
    except Exception as e:
        print(e)
        return jsonify( {'error': "Error en eliminacion de la mascota"}), 500

def updateMascotaUsuario(userId, id):
    try:
        # consultamos la mascota en la base de datos antes de actualizar
        mascota_id = str(id)
        if mascota_id:
            mascota = database.reference(f"/usuarios/{userId}/mascotas/{id}").get()
            if mascota:
                # se actualiza el cliente en la base de datos con lo que llegue en el request json
                database.reference(f"/usuarios/{userId}/mascotas").child(mascota_id).update(request.json)
                return jsonify({'message': "Actualizacion realizada"}), 200
            else: 
                return jsonify({'message': "Mascota no encontrada para actualizar"}), 404
        else: 
            return jsonify({'message': "Debes enviar un id de la mascota"}), 404

    except Exception as e:
        print(e)
        return jsonify( {'error': "Error en actualizacion de la mascota"}), 500

def registrarAccionMascota(userId, nombreMascota):
    try:
        pathMascota = f"/usuarios/{str(userId)}/mascotas/{nombreMascota}"
        mascota = database.reference(pathMascota).get()
        if mascota:

            if "accion" in request.json:

                lista_acciones = database.reference(f"{pathMascota}/acciones").get()
                index = 0
                if lista_acciones:
                    index = len(lista_acciones)
                    print(f"cant: ${len(lista_acciones)}")
                
                accion = str(request.json["accion"])
                today = datetime.today()
                
                nuevaAccion = {
                    "index": str(index),
                    "fecha": today.strftime('%Y-%m-%d'),
                    "hora": today.strftime('%H:%M:%S'),
                    "accion": accion
                }

                database.reference(f"{pathMascota}/acciones").child(str(index)).set(nuevaAccion)
                return jsonify(nuevaAccion), 201
            else: 
                return jsonify({'message': "Data incompleta"}), 400
        else:
            return jsonify({'error': "Mascota no encontrada"}), 404
    except Exception as e:
        print(e)
        return jsonify( {'error': "Error en creacion de la accion"}), 500

def listarAccionesMascota(userId, nombreMascota):
    try:
        pathMascota = f"/usuarios/{str(userId)}/mascotas/{nombreMascota}"
        mascota = database.reference(pathMascota).get()
        if mascota:
            
            lista_acciones = database.reference(f"{pathMascota}/acciones").get()
            if lista_acciones:                
                return jsonify(lista_acciones), 200
            else:
                return jsonify([]), 200
        else:
            return jsonify({'error': "Mascota no encontrada"}), 404
    except Exception as e:
        print(e)
        return jsonify({'error': "Error en consulta de listado de acciones de la mascota"}), 500

# comida
# agua
# afuera
# jugar
# mimos
# aburrido
# miedo
# si
# no
