from flask import Blueprint, json, render_template, request, redirect, flash, session
import requests

user_view = Blueprint('user_view', __name__)

def get_session():
    return session

@user_view.context_processor
def inject_session():
    return dict(sesion_templates=session)

@user_view.route('/')
def index():
    return render_template('/parts/users/login.html')

@user_view.route('/home')
def home():
    if 'usuario' not in session:
        flash('Debe iniciar sesión para acceder a esta página', 'error')
        return redirect('/login')
    return render_template('home.html')

@user_view.route('/login')
def login():
    return render_template('/parts/users/login.html')

@user_view.route('/registro')
def registro():
    return render_template('/parts/users/register.html')

@user_view.route('/registro/save', methods=['POST'])
def save_user():
    headers = {'Content-Type': 'application/json'}
    data_form = {
        'nombres': request.form['nombres'],
        'apellidos': request.form['apellidos'],
        'fecha_nacimiento': request.form['fecha_nacimiento'],
        'email': request.form['email'],
        'celular': request.form['celular'],
        'usuario': request.form['usuario'],
        'contrasena': request.form['contrasena']
    }

    print(data_form)
    r = requests.post('http://localhost:5000/bd/registro/save', data=json.dumps(data_form), headers=headers)
    print(r)
    data = r.json().get('data')
    if r.status_code == 200:
        flash('Usuario registrado correctamente', 'success')
        return redirect('/login')
    else:
        flash('Error al registrar en la base de datos: ' + str(data), 'error')
        return redirect(request.referrer)
    
@user_view.route('/login', methods=['POST'])
def login_user():
    headers = {'Content-Type': 'application/json'}
    data_form = {
        'usuario': request.form['usuario'],
        'contrasena': request.form['contrasena']
    }

    r = requests.post('http://localhost:5000/bd/login', data=json.dumps(data_form), headers=headers)
    data = r.json().get('data')
    if r.status_code == 200:
        print(data)
        r2 = requests.get(f'http://localhost:5000/bd/personas/{int(data["identificacion"])}')
        data2 = r2.json().get('data')
        print(data2)

        session['rol'] = data2.get('id_rol')
        session['usuario'] = data.get('usuario')
        session['persona'] = data2

        print(session)
        flash('Usuario logeado correctamente', 'success')
        return redirect('/home')
    else:
        flash('Error al logear en la base de datos: ' + str(data), 'error')
        return redirect(request.referrer)
    
@user_view.route('/pacientes/all')
def get_personas():
    if 'usuario' not in session:
        flash('Debe iniciar sesión para acceder a esta página', 'error')
        return redirect('/login')
    if session['rol'] == 3:
        flash('No tiene permisos para acceder a esta página', 'error')
        return redirect('/home')
    r = requests.get('http://localhost:5000/bd/personas/all')
    data = r.json().get('data')
    if r.status_code == 200:
        return render_template('/parts/users/list_persons.html', personas=data)
    else:
        flash('Error al obtener las personas: ' + str(data), 'error')
        return redirect(request.referrer)
    
@user_view.route('/pacientes/<int:id>')
def get_persona(id):
    if 'usuario' not in session:
        flash('Debe iniciar sesión para acceder a esta página', 'error')
        return redirect('/login')
    r = requests.get(f'http://localhost:5000/bd/personas/{id}')
    data = r.json().get('data')
    if r.status_code == 200:
        return render_template('/parts/users/detail_person.html', paciente=data)
    else:
        flash('Error al obtener la persona: ' + str(data), 'error')
        return redirect(request.referrer)
    
@user_view.route('/pacientes/update', methods=['POST'])
def update_persona():
    if 'usuario' not in session:
        flash('Debe iniciar sesión para acceder a esta página', 'error')
        return redirect('/login')
    
    headers = {'Content-Type': 'application/json'}
    data_form = {
        'id' : request.form['id'],
        'nombres': request.form['nombres'],
        'apellidos': request.form['apellidos'],
        'email': request.form['email'],
        'celular': request.form['celular']
    }
    #print(data_form)

    r = requests.put(f'http://localhost:5000/bd/personas/update', data=json.dumps(data_form), headers=headers)
    data = r.json().get('data')
    if r.status_code == 200:
        flash('Persona actualizada correctamente', 'success')
        return redirect('/pacientes/all')
    else:
        flash('Error al actualizar la persona: ' + str(data), 'error')
        return redirect(request.referrer)
    
@user_view.route('/pacientes/delete', methods=['POST'])
def delete_persona():
    if 'usuario' not in session:
        flash('Debe iniciar sesión para acceder a esta página', 'error')
        return redirect('/login')
    if session['rol'] != 1:
        flash('No tiene permisos para acceder a esta página', 'error')
        return redirect('/home')
    
    id = request.form['id']
    r = requests.delete(f'http://localhost:5000/bd/personas/delete', data=json.dumps({'id': id}), headers={'Content-Type': 'application/json'})
    data = r.json().get('data')
    if r.status_code == 200:
        flash('Persona eliminada correctamente', 'success')
        return redirect('/pacientes/all')
    else:
        flash('Error al eliminar la persona: ' + str(data), 'error')
        return redirect(request.referrer)

@user_view.route('/pacientes/updateRol', methods=['POST'])
def update_rol():
    if 'usuario' not in session:
        flash('Debe iniciar sesión para acceder a esta página', 'error')
        return redirect('/login')
    if session['rol'] != 1:
        flash('No tiene permisos para acceder a esta página', 'error')
        return redirect('/home')
    headers = {'Content-Type': 'application/json'}
    data_form = {
        'id_usuario' : request.form['id_usuario'],
        'id_rol': request.form['id_rol']
    }
    #print(data_form)

    r = requests.patch(f'http://localhost:5000/bd/personas/updateRol', data=json.dumps(data_form), headers=headers)
    data = r.json().get('data')
    if r.status_code == 200:
        flash('Rol actualizado correctamente', 'success')
        return redirect('/pacientes/all')
    else:
        flash('Error al actualizar el rol: ' + str(data), 'error')
        return redirect(request.referrer)
    
@user_view.route('/logout')
def logout():
    session.clear()
    return redirect('/login')
