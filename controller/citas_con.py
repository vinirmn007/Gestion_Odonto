import datetime
import time
from flask import Blueprint, json, render_template, request, redirect, url_for, flash, jsonify
from config import mysql

citas_controller = Blueprint('citas_controller', __name__)

@citas_controller.route('/bd/citas/<string:estado>', methods=['GET'])
def db_get_citas(estado):
    try:
        cur = mysql.connection.cursor()
        cur.execute(f"SELECT * FROM CitaMedica WHERE estado = '{estado}'")
        data = cur.fetchall()
        cur.close()
        citas = []
        print("Datos obtenidos de la BD:", data) 
        for row in data:
            row['fecha'] = row['fecha'].strftime('%Y-%m-%d') if isinstance(row['fecha'], datetime.date) else str(row['fecha'])
            row['hora'] = str(datetime.timedelta(seconds=row['hora'].seconds)) if isinstance(row['hora'], datetime.timedelta) else str(row['hora'])

        print("Datos procesados para JSON:", data) 


        return jsonify({'msg': 'Ok', 'data': data}), 200
    except Exception as e:
        return jsonify({'msg': 'Error', 'data': str(e)}), 400
    

@citas_controller.route('/bd/citas/save', methods=['POST'])
def db_save_cita():
    data = request.json
    print('OBTENGO EL JSON')
    print(data)
    
    try:
        cur = mysql.connection.cursor() #Comenzar el cursor sql
        #Insertar
        cur.execute(
            "INSERT INTO CitaMedica (motivo, observaciones, fecha, hora, iden_paciente, iden_odontologo) VALUES (%s, %s, %s, %s, %s, %s)",
            (data['motivo'], data['observaciones'], data['fecha'], data['hora'], data['iden_paciente'], data['iden_odontologo']))
        #Guardar
        mysql.connection.commit()
        cur.close()
        
        return jsonify({'msg': 'Ok', 'data': 'cita registrad correctamente'}), 200
    except Exception as e:
        print('llego al error')
        print(e)
        return jsonify({'msg': 'Error', 'data': str(e)}), 400


@citas_controller.route('/bd/citas/update', methods=['PUT'])
def db_update_cita():
    data = request.json
    print(data['codigo_cita'])
    
    try:
        cur = mysql.connection.cursor()
        cur.execute(
            """UPDATE CitaMedica 
            SET motivo = %s, observaciones = %s, fecha = %s, hora = %s, iden_paciente = %s, iden_odontologo = %s 
            WHERE codigo_cita = %s""",
            (data['motivo'], data['observaciones'], data['fecha'], data['hora'], data['iden_paciente'], 1, int(data['codigo_cita']))
        )
        print(data)
        mysql.connection.commit()
        cur.close()

        return jsonify({'msg': 'Ok', 'data': 'Cita actualizada correctamente'}), 200
    except Exception as e:
        return jsonify({'msg': 'Error', 'data': str(e)}), 400

@citas_controller.route('/bd/citas/delete', methods=['DELETE'])
def db_delete_cita():
    data = request.json
    try:
    
        if 'codigo_cita' not in data:
            return jsonify({'msg': 'Error', 'data': 'Falta el campo "codigo_cita"'}), 400

        
        cur = mysql.connection.cursor()
        cur.execute(f"DELETE FROM CitaMedica WHERE codigo_cita = {int(data['codigo_cita'])}")
        mysql.connection.commit()
        cur.close()

        return jsonify({'msg': 'Ok', 'data': 'Cita eliminada correctamente'}), 200
    except Exception as e:
        return jsonify({'msg': 'Error', 'data': str(e)}), 400
