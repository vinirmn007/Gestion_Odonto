from flask import Blueprint, json, render_template, request, redirect, url_for, flash, jsonify
from config import mysql

receta_controller = Blueprint('receta_controller', __name__)

@receta_controller.route('/bd/receta/all', methods=['GET'])
def db_get_recetas():
    try:
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM Receta")
        data = cur.fetchall()
        cur.close()

        return jsonify({'msg': 'Ok', 'data': data}), 200
    except Exception as e:
        return jsonify({'msg': 'Error', 'data': str(e)}), 400

@receta_controller.route('/bd/receta/<int:codigo_receta>', methods=['GET'])
def db_get_receta(codigo_receta):
    try:
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM Receta WHERE codigo_receta = %s", (codigo_receta,))
        data = cur.fetchone()
        cur.close()

        return jsonify({'msg': 'Ok', 'data': data}), 200
    except Exception as e:
        return jsonify({'msg': 'Error', 'data': str(e)}), 400
    
@receta_controller.route('/bd/receta/save', methods=['POST'])
def db_save_receta():
    data = request.json
    try:
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO Receta (dosis, medicamento, cod_diagnostico) VALUES (%s, %s, %s)",
                    (data['dosis'], data['medicamento'], data['cod_diagnostico']))
        mysql.connection.commit()
        cur.close()

        return jsonify({'msg': 'Ok', 'data': 'Receta registrada correctamente'}), 200
    except Exception as e:
        return jsonify({'msg': 'Error', 'data': str(e)}), 400
    
@receta_controller.route('/bd/receta/delete', methods=['DELETE'])
def db_delete_receta():
    data = request.json
    try:
        cur = mysql.connection.cursor()
        cur.execute("DELETE FROM Receta WHERE codigo_receta = %s", (data['codigo_receta'],))
        mysql.connection.commit()
        cur.close()

        return jsonify({'msg': 'Ok', 'data': 'Receta eliminada correctamente'}), 200
    except Exception as e:
        return jsonify({'msg': 'Error', 'data': str(e)}), 400
    
@receta_controller.route('/bd/receta/update', methods=['PUT'])
def db_update_receta():
    data = request.json
    try:
        cur = mysql.connection.cursor()
        cur.execute("UPDATE Receta SET dosis = %s, medicamento = %s, cod_diagnostico = %s WHERE codigo_receta = %s",
                    (data['dosis'], data['medicamento'], data['cod_diagnostico'], data['codigo_receta']))
        mysql.connection.commit()
        cur.close()

        return jsonify({'msg': 'Ok', 'data': 'Receta actualizada correctamente'}), 200
    except Exception as e:
        return jsonify({'msg': 'Error', 'data': str(e)}), 400
