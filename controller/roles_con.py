from flask import Blueprint, json, render_template, request, redirect, url_for, flash, jsonify
from config import mysql

roles_controller = Blueprint('roles_controller', __name__)

@roles_controller.route('/bd/roles/all', methods=['GET'])
def db_get_roles():
    try:
        cur = mysql.connection.cursor()
        cur.execute(f"SELECT * FROM Rol")
        data = cur.fetchall()
        cur.close()

        return jsonify({'msg': 'Ok', 'data': data}), 200
    except Exception as e:
        return jsonify({'msg': 'Error', 'data': str(e)}), 400

@roles_controller.route('/bd/roles/<int:id>', methods=['GET'])
def db_get_rol(id):
    try:
        cur = mysql.connection.cursor()
        cur.execute(f"SELECT * FROM Rol WHERE id = {id}")
        data = cur.fetchone()
        cur.close()

        return jsonify({'msg': 'Ok', 'data': data}), 200
    except Exception as e:
        return jsonify({'msg': 'Error', 'data': str(e)}), 400
    
@roles_controller.route('/bd/roles/save', methods=['POST'])
def db_save_rol():
    data = request.json

    try:
        cur = mysql.connection.cursor()
        cur.execute(f"INSERT INTO Rol (nombre, descripcion) VALUES ('{data['nombre']}', '{data['descripcion']}')")
        mysql.connection.commit()
        cur.close()

        return jsonify({'msg': 'Ok', 'data': 'Rol registrado correctamente'}), 200
    except Exception as e:
        return jsonify({'msg': 'Error', 'data': str(e)}), 400
    
@roles_controller.route('/bd/roles/delete/<int:id>', methods=['DELETE'])
def db_delete_rol(id):
    try:
        cur = mysql.connection.cursor()
        cur.execute(f"DELETE FROM Rol WHERE id = {id}")
        mysql.connection.commit()
        cur.close()

        return jsonify({'msg': 'Ok', 'data': 'Rol eliminado correctamente'}), 200
    except Exception as e:
        return jsonify({'msg': 'Error', 'data': str(e)}), 400