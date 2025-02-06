from flask import Blueprint, json, render_template, request, redirect, url_for, flash
import requests

login_view = Blueprint('login_view', __name__)

@login_view.route('/')
def index():
    return render_template('/parts/users/login.html')

@login_view.route('/home')
def home():
    return render_template('home.html')

@login_view.route('/login')
def login():
    return render_template('/parts/users/login.html')

@login_view.route('/registro')
def registro():
    return render_template('/parts/users/register.html')

@login_view.route('/registro/save', methods=['POST'])
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
        return redirect('/home')
    else:
        flash('Error al registrar en la base de datos: ' + str(data), 'error')
        return redirect(request.referrer)