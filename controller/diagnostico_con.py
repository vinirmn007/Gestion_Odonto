from flask import Blueprint, json, render_template, request, redirect, url_for, flash, jsonify
from config import mysql

diagnostico_controller = Blueprint('diagnostico_controller', __name__)

@diagnostico_controller.route('/bd/diagnostico/all', methods=['GET'])
def db_get_diagnosticos():
    try:
        cur = mysql.connection.cursor()
        cur.execute(f"SELECT * FROM Diagnostico")
        data = cur.fetchall()
        cur.close()

        return jsonify({'msg': 'Ok', 'data': data}), 200
    except Exception as e:
        return jsonify({'msg': 'Error', 'data': str(e)}), 400

@diagnostico_controller.route('/bd/diagnostico/<int:codigo_diagnostico>', methods=['GET'])
def db_get_diagnostico(codigo_diagnostico):
    try:
        cur = mysql.connection.cursor()
        cur.execute(f"SELECT * FROM Diagnostico WHERE codigo_diagnostico = {codigo_diagnostico}")
        data = cur.fetchone()
        cur.close()

        return jsonify({'msg': 'Ok', 'data': data}), 200
    except Exception as e:
        return jsonify({'msg': 'Error', 'data': str(e)}), 400
    
@diagnostico_controller.route('/bd/diagnostico/save', methods=['POST'])
def db_save_diagnostico():
    data = request.json

    try:
        cur = mysql.connection.cursor()
        cur.execute(f"INSERT INTO Diagnostico (descripcion, examen, cod_cita) VALUES ('{data['descripcion']}', '{data['examen']}', {data['cod_cita']})")
        mysql.connection.commit()
        cur.close()

        return jsonify({'msg': 'Ok', 'data': 'Diagnostico registrado correctamente'}), 200
    except Exception as e:
        return jsonify({'msg': 'Error', 'data': str(e)}), 400
    
@diagnostico_controller.route('/bd/diagnostico/delete', methods=['DELETE'])
def db_delete_diagnostico():
    data = request.json
    try:
        cur = mysql.connection.cursor()
        cur.execute(f"DELETE FROM Diagnostico WHERE codigo_diagnostico = {int(data['codigo_diagnostico'])}")
        mysql.connection.commit()
        cur.close()

        return jsonify({'msg': 'Ok', 'data': 'Diagnostico eliminado correctamente'}), 200
    except Exception as e:
        return jsonify({'msg': 'Error', 'data': str(e)}), 400
    
@diagnostico_controller.route('/bd/diagnostico/update', methods=['PUT'])
def db_update_diagnostico():
    data = request.json
    print(data['codigo_diagnostico'])
    
    try:
        cur = mysql.connection.cursor()
        cur.execute(f"UPDATE Diagnostico SET descripcion = '{data['descripcion']}', examen = '{data['examen']}', cod_cita = '{data['cod_cita']}' WHERE codigo_diagnostico = {int(data['codigo_diagnostico'])}")
        mysql.connection.commit()
        cur.close()

        return jsonify({'msg': 'Ok', 'data': 'Diagnostico actualizado correctamente'}), 200
    except Exception as e:
        return jsonify({'msg': 'Error', 'data': str(e)}), 400