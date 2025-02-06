from flask import Blueprint, json, render_template, request, redirect, url_for, flash, jsonify

#Importar el mysql
from config import mysql

user_controller = Blueprint('user_controller', __name__)

@user_controller.route('/bd/registro/save', methods=['POST'])
def db_regis_user():
    data = request.json
    print('OBTENGO EL JSON')
    print(data)
    
    try:
        cur = mysql.connection.cursor() #Comenzar el cursor sql
        #Insertar
        cur.execute(f"INSERT INTO Persona (nombres, apellidos, fecha_nacimiento, email, celular) VALUES ('{data['nombres']}', '{data['apellidos']}', '{data['fecha_nacimiento']}', '{data['email']}', '{data['celular']}')")

        iden_persona = cur.lastrowid #Obtener el id de persona

        cur.execute(f"INSERT INTO Cuenta (identificacion, usuario, contrasena) VALUES ('{iden_persona}', '{data['usuario']}', '{data['contrasena']}')")
        #Guardar
        mysql.connection.commit()
        cur.close()
        
        return jsonify({'msg': 'Ok', 'data': 'Usuario registrado correctamente'}), 200
    except Exception as e:
        print('llego al error')
        print(e)
        return jsonify({'msg': 'Error', 'data': str(e)}), 400

@user_controller.route('/bd/login', methods=['POST'])
def db_login_user():
    data = request.json

    cur = mysql.connection.cursor()
    cur.execute(f"SELECT * FROM Cuenta WHERE usuario = '{data['usuario']}' AND contrasena = '{data['contrasena']}'")
    data = cur.fetchone()
    cur.close()

    if data:
        return jsonify({'msg': 'Ok', 'data': 'Usuario logeado correctamente'}), 200
    else:
        return jsonify({'msh': 'Error', 'data': 'Usuario o contraseña incorrecta'}), 400
    
@user_controller.route('/bd/personas/all', methods=['GET'])
def db_get_personas():
    try:
        cur = mysql.connection.cursor()
        cur.execute(f"SELECT * FROM Persona")
        data = cur.fetchall()
        cur.close()

        return jsonify({'msg': 'Ok', 'data': data}), 200
    except Exception as e:
        return jsonify({'msg': 'Error', 'data': str(e)}), 400
    
@user_controller.route('/bd/personas/<int:id>', methods=['GET'])
def db_get_persona(id):
    try:
        cur = mysql.connection.cursor()
        cur.execute(f"SELECT * FROM Persona WHERE identificacion = {id}")
        data = cur.fetchone()
        cur.close()

        return jsonify({'msg': 'Ok', 'data': data}), 200
    except Exception as e:
        return jsonify({'msg': 'Error', 'data': str(e)}), 400
    
@user_controller.route('/bd/personas/update', methods=['PUT'])
def db_update_persona():
    data = request.json
    print(data['id'])
    
    try:
        cur = mysql.connection.cursor()
        cur.execute(f"UPDATE Persona SET nombres = '{data['nombres']}', apellidos = '{data['apellidos']}', email = '{data['email']}', celular = '{data['celular']}' WHERE identificacion = {int(data['id'])}")
        mysql.connection.commit()
        cur.close()

        return jsonify({'msg': 'Ok', 'data': 'Persona actualizada correctamente'}), 200
    except Exception as e:
        return jsonify({'msg': 'Error', 'data': str(e)}), 400
    
@user_controller.route('/bd/personas/delete', methods=['DELETE'])
def db_delete_persona():
    data = request.json
    try:
        cur = mysql.connection.cursor()
        cur.execute(f"DELETE FROM Cuenta WHERE identificacion = {int(data['id'])}")
        cur.execute(f"DELETE FROM Persona WHERE identificacion = {int(data['id'])}")
        mysql.connection.commit()
        cur.close()

        return jsonify({'msg': 'Ok', 'data': 'Persona eliminada correctamente'}), 200
    except Exception as e:
        return jsonify({'msg': 'Error', 'data': str(e)}), 400