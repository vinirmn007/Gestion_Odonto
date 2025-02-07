from flask import Blueprint, json, render_template, request, redirect, url_for, flash, jsonify
from config import mysql

odon_controller = Blueprint('odon_controller', __name__)

@odon_controller.route('/bd/odontologo/save', methods=['POST'])
def db_regis_odon():
    data = request.json
    print('OBTENGO EL JSON')
    print(data)
    
    try:
        cur = mysql.connection.cursor()
        cur.execute(f"INSERT INTO Odontologo (identificacion_odon, codigo_licencia) VALUES ('{data['usuario_id']}', '{data['codigo_licencia']}')")
        cur.execute(f"UPDATE Persona SET id_rol = 2 WHERE identificacion = '{data['usuario_id']}'")
        mysql.connection.commit()
        cur.close()
        
        return jsonify({'msg': 'Ok', 'data': 'Odontologo registrado correctamente'}), 200
    except Exception as e:
        print('llego al error')
        print(e)
        return jsonify({'msg': 'Error', 'data': str(e)}), 400
    
@odon_controller.route('/bd/odontologo/all', methods=['GET'])
def db_get_all_odon():
    try:
        cur = mysql.connection.cursor()
        cur.execute("SELECT P.*, O.codigo_licencia FROM Persona P INNER JOIN Odontologo O ON P.identificacion = O.identificacion_odon")
        data = cur.fetchall()
        cur.close()
        
        return jsonify({'msg': 'Ok', 'data': data}), 200
    except Exception as e:
        return jsonify({'msg': 'Error', 'data': str(e)}), 400