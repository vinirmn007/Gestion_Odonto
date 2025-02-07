from flask import Blueprint, json, render_template, request, redirect, flash
import requests
from .users_view import get_session

roles_view = Blueprint('roles_view', __name__)

sesion = get_session()

@roles_view.context_processor
def inject_session():
    return dict(sesion_templates=sesion)

@roles_view.route('/admin')
def admin():
    if 'usuario' not in sesion:
        flash('Debe iniciar sesión para acceder a esta página', 'error')
        return redirect('/login')
    if sesion['rol'] != 1:
        flash('No tiene permisos para acceder a esta página', 'error')
        return redirect('/home')
    r = requests.get('http://localhost:5000/bd/personas/all')
    data = r.json().get('data')

    rRoles = requests.get('http://localhost:5000/bd/roles/all')
    dataRoles = rRoles.json().get('data')

    if r.status_code == 200:
        return render_template('/parts/admin/admin.html', usuarios=data, roles=dataRoles)
    else:
        flash('Error al obtener las personas: ' + str(data), 'error')
        return redirect(request.referrer)
    
@roles_view.route('/admin/roles/save', methods=['POST'])
def save_rol():
    if 'usuario' not in sesion:
        flash('Debe iniciar sesión para acceder a esta página', 'error')
        return redirect('/login')
    if sesion['rol'] != 1:
        flash('No tiene permisos para acceder a esta página', 'error')
        return redirect('/home')
    headers = {'Content-Type': 'application/json'}
    data_form = {
        'nombre': request.form['nombre'],
        'descripcion': request.form['descripcion']
    }

    r = requests.post('http://localhost:5000/bd/roles/save', data=json.dumps(data_form), headers=headers)
    data = r.json().get('data')
    if r.status_code == 200:
        flash('Rol registrado correctamente', 'success')
        return redirect('/admin')
    else:
        flash('Error al registrar en la base de datos: ' + str(data), 'error')
        return redirect(request.referrer)
    
@roles_view.route('/admin/roles/delete/<int:id>', methods=['GET'])
def delete_rol(id):
    if 'usuario' not in sesion:
        flash('Debe iniciar sesión para acceder a esta página', 'error')
        return redirect('/login')
    if sesion['rol'] != 1:
        flash('No tiene permisos para acceder a esta página', 'error')
        return redirect('/home')
    r = requests.delete(f'http://localhost:5000/bd/roles/delete/{id}')
    data = r.json().get('data')
    if r.status_code == 200:
        flash('Rol eliminado correctamente', 'success')
        return redirect('/admin')
    else:
        flash('Error al eliminar en la base de datos: ' + str(data), 'error')
        return redirect(request.referrer)
