from flask import Blueprint, json, render_template, request, redirect, flash, session
import requests
from .users_view import get_session

# Vista para Historial Médico
historialMedico_view = Blueprint('historialMedico_view', __name__)
@historialMedico_view.route('/historial/form')
def form_historial():
    return render_template('/parts/historial/form_historial.html')


sesion = get_session()

@historialMedico_view.context_processor
def inject_session():
    return dict(sesion_templates=sesion)

@historialMedico_view.route('/historial/all')
def get_historiales():
    r = requests.get('http://localhost:5000/bd/historial/all')
    data = r.json().get('data')
    if r.status_code == 200:
        return render_template('/parts/historial/list_historial.html', historiales=data)
    else:
        flash('Error al obtener los historiales médicos: ' + str(data), 'error')
        return redirect(request.referrer)

@historialMedico_view.route('/historial/<int:codigo_historial>')
def get_historial(codigo_historial):
    r = requests.get(f'http://localhost:5000/bd/historial/{codigo_historial}')
    data = r.json().get('data')
    if r.status_code == 200:
        return render_template('/parts/historial/detail_historial.html', historial=data)
    else:
        flash('Error al obtener el historial médico: ' + str(data), 'error')
        return redirect(request.referrer)

@historialMedico_view.route('/historial/save', methods=['POST'])
def save_historial():
    headers = {'Content-Type': 'application/json'}
    data_form = {
        'patologias_pasadas': request.form['patologias_pasadas'],
        'alergias': request.form['alergias'],
        'tratamiento': request.form['tratamiento']
    }
    r = requests.post('http://localhost:5000/bd/historial/save', data=json.dumps(data_form), headers=headers)
    data = r.json().get('data')
    if r.status_code == 200:
        flash('Historial médico registrado correctamente', 'success')
        return redirect('/historial/all')
    else:
        flash('Error al registrar el historial médico: ' + str(data), 'error')
        return redirect(request.referrer)

@historialMedico_view.route('/historial/update', methods=['POST'])
def update_historial():
    headers = {'Content-Type': 'application/json'}
    data_form = {

        'codigo_historial': request.form['codigo_historial'],
        'patologias_pasadas': request.form['patologias_pasadas'],
        'alergias': request.form['alergias'],
        'tratamiento': request.form['tratamiento']
    }
    r = requests.put('http://localhost:5000/bd/historial/update', data=json.dumps(data_form), headers=headers)
    data = r.json().get('data')
    if r.status_code == 200:
        flash('Historial médico actualizado correctamente', 'success')
        return redirect('/historial/all')
    else:
        flash('Error al actualizar el historial médico: ' + str(data), 'error')
        return redirect(request.referrer)

@historialMedico_view.route('/historial/delete', methods=['POST'])
def delete_historial():
    codigo_historial = request.form['codigo_historial']
    r = requests.delete('http://localhost:5000/bd/historial/delete', data=json.dumps({'codigo_historial': codigo_historial}), headers={'Content-Type': 'application/json'})
    data = r.json().get('data')
    if r.status_code == 200:
        flash('Historial médico eliminado correctamente', 'success')
        return redirect('/historial/all')
    else:
        flash('Error al eliminar el historial médico: ' + str(data), 'error')
        return redirect(request.referrer)
