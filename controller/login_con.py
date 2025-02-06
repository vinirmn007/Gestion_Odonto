from flask import Blueprint, json, render_template, request, redirect, url_for, flash, jsonify

#Importar el mysql
from config import mysql

login_controller = Blueprint('login_controller', __name__)

@login_controller.route('/registro', methods=['POST'])
def regis_user():
    nombres = request.form['nombres']
    apellidos = request.form['apellidos']
    fecha_nacimiento = request.form['fecha_nacimiento']
    email = request.form['email']
    celular = request.form['celular']

    usuario = request.form['usuario']
    contrasena = request.form['contrasena']
    
    cur = mysql.connection.cursor() #Comenzar el cursor sql
    #Insertar
    cur.execute(f"INSERT INTO Persona (nombres, apellidos, fecha_nacimiento, email, celular) VALUES ('{nombres}', '{apellidos}', '{fecha_nacimiento}', '{email}', '{celular}')")

    iden_persona = cur.lastrowid #Obtener el id de persona

    cur.execute(f"INSERT INTO Cuenta (identificacion, usuario, contrasena) VALUES ('{iden_persona}', '{usuario}', '{contrasena}')")
    #Guardar
    mysql.connection.commit()
    cur.close()
    
    return jsonify({'message': 'Usuario registrado correctamente'}), 200