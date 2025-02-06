from flask import Blueprint, json, render_template, request, redirect, url_for, flash, jsonify

#Importar el mysql
from config import mysql

user_controller = Blueprint('user_controller', __name__)

@user_controller.route('/bd/registro/save', methods=['POST'])
def regis_user():
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

@user_controller.route('/login', methods=['POST'])
def login_user():
    usuario = request.form['usuario']
    contrasena = request.form['contrasena']

    cur = mysql.connection.cursor()
    cur.execute(f"SELECT * FROM Cuenta WHERE usuario = '{usuario}' AND contrasena = '{contrasena}'")
    data = cur.fetchone()
    cur.close()

    if data:
        return jsonify({'message': 'Usuario logeado correctamente'}), 200
    else:
        return jsonify({'message': 'Usuario o contraseña incorrecta'}), 400
