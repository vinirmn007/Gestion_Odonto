from flask import Blueprint, json, render_template, request, redirect, url_for, flash, jsonify
import requests
from config import mysql

# Controlador de API para Historial Médico
historialMedico_controller = Blueprint('historialMedico_controller', __name__)

@historialMedico_controller.route('/bd/historial/all', methods=['GET'])
def db_ALL_HISTORIAL():
    try:
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM HistorialMedico")
        data = cur.fetchall()
        cur.close()
        
        return jsonify({'msg': 'Ok', 'data': data}), 200
    except Exception as e:
        return jsonify({'msg': 'Error', 'data': str(e)}), 400

@historialMedico_controller.route('/bd/historial/save', methods=['POST'])
def db_regis_user():
    data = request.json
    try:
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO HistorialMedico (patologias_pasadas, alergias, tratamiento) VALUES (%s, %s, %s)", 
                    (data['patologias_pasadas'], data['alergias'], data['tratamiento']))
        mysql.connection.commit()
        cur.close()
        
        return jsonify({'msg': 'Ok', 'data': 'Historial médico registrado correctamente'}), 200
    except Exception as e:
        return jsonify({'msg': 'Error', 'data': str(e)}), 400

@historialMedico_controller.route('/bd/historial/<int:codigo_historial>', methods=['GET'])
def db_get_codigo_historial(codigo_historial):
    try:
        cur = mysql.connection.cursor()
        cur.execute(f"SELECT * FROM HistorialMedico WHERE codigo_historial = {codigo_historial}") 
        data = cur.fetchone()
        cur.close()
        
        return jsonify({'msg': 'Ok', 'data': data}), 200
    except Exception as e:
        return jsonify({'msg': 'Error', 'data': str(e)}), 400

@historialMedico_controller.route('/bd/historial/update', methods=['PUT'])
def db_update_historial():
    data = request.json
    print(data['codigo_historial'])

    try:
        cur = mysql.connection.cursor()
        cur.execute(f"UPDATE HistorialMedico SET patologias_pasadas = '{data['patologias_pasadas']}',alergias = '{data['alergias']}', tratamiento = '{data['tratamiento']}'wHERE codigo_historial = {int(data['codigo_historial'])}")
        mysql.connection.commit()
        cur.close()
        
        return jsonify({'msg': 'Ok', 'data': 'Historial médico actualizado correctamente'}), 200
    except Exception as e:
        return jsonify({'msg': 'Error', 'data': str(e)}), 400

@historialMedico_controller.route('/bd/historial/delete', methods=['DELETE'])
def db_delete_historial():
    data = request.json
    try:
        cur = mysql.connection.cursor()
        cur.execute("DELETE FROM HistorialMedico WHERE codigo_historial = %s", (data['codigo_historial'],))
        mysql.connection.commit()
        cur.close()
        
        return jsonify({'msg': 'Ok', 'data': 'Historial médico eliminado correctamente'}), 200
    except Exception as e:
        return jsonify({'msg': 'Error', 'data': str(e)}), 400
