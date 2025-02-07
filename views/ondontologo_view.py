from flask import Blueprint, json, render_template, request, redirect, flash
import requests
from .users_view import get_session

odonto_view = Blueprint('odonto_view', __name__)

sesion = get_session()

@odonto_view.context_processor
def inject_session():
    return dict(sesion_templates=sesion)

@odonto_view.route('/admin/odontologos/save', methods=['POST'])
def save_odonto():
    if 'usuario' not in sesion:
        flash('Debe iniciar sesión para acceder a esta página', 'error')
        return redirect('/login')
    if sesion['rol'] != 1:
        flash('No tiene permisos para acceder a esta página', 'error')
        return redirect('/home')
    headers = {'Content-Type': 'application/json'}
    data_form = {
        'usuario_id': request.form['usuario_id'],
        'codigo_licencia': request.form['codigo_licencia']
    }

    r = requests.post('http://localhost:5000/bd/odontologo/save', data=json.dumps(data_form), headers=headers)
    data = r.json().get('data')
    if r.status_code == 200:
        flash('Odontologo registrado correctamente', 'success')
        return redirect('/admin')
    else:
        flash('Error al registrar en la base de datos: ' + str(data), 'error')
        return redirect(request.referrer)