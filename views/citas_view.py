from flask import Blueprint, json, render_template, request, redirect, flash, session
import requests

citas_view = Blueprint('citas_view', __name__)

@citas_view.route('/citas/<string:estado>', methods=['GET'])
def get_citas(estado):
    r = requests.get(f'http://localhost:5000/bd/citas/{estado}')
    rp = requests.get('http://localhost:5000/bd/personas/all')
    data = r.json().get('data')
    if r.status_code == 200:
        return render_template('/parts/citas/list_citas.html', citas=data, personas=rp.json().get('data'))
    else:
        flash('Error al obtener las citas: ' + str(data), 'error')
        return redirect(request.referrer)
    

@citas_view.route('/citas/save', methods=['GET', 'POST'] )
def save_citas():
    headers = {'Content-Type': 'application/json'}
    if request.method == 'POST':
        data_form = {
            'motivo': request.form['motivo'],
            'observaciones': request.form['observaciones'],
            'fecha': request.form['fecha'],
            'hora': request.form['hora'],
            'iden_paciente': request.form['iden_paciente'],
        }
        print(data_form)
        r = requests.post('http://localhost:5000/bd/citas/save', data=json.dumps(data_form), headers=headers)
        print(r)
        data = r.json().get('data')
        if r.status_code == 200:
            flash('Usuario registrado correctamente', 'success')
            return redirect('/citas/EN_ESPERA')
        else:
            flash('Error al registrar en la base de datos: ' + str(data), 'error')
            return redirect(request.referrer)
    
    rp = requests.get('http://localhost:5000/bd/personas/all')
    return render_template('/parts/citas/save_citas.html', personas= rp.json().get('data'))


@citas_view.route('/citas/update', methods=['POST'])
def update_cita():
    headers = {'Content-Type': 'application/json'}
    
    data_form = {
        'codigo_cita': request.form['codigo_cita'],
        'motivo': request.form['motivo'],
        'observaciones': request.form['observaciones'],
        'fecha': request.form['fecha'],
        'hora': request.form['hora'],
        'iden_paciente': request.form['iden_paciente']
    }


    try:
        r = requests.put(f'http://localhost:5000/bd/citas/update', data=json.dumps(data_form), headers=headers)
        r.raise_for_status()  
        data = r.json().get('data')

        if r.status_code == 200:
            flash('Cita actualizada correctamente', 'success')
            return redirect('/citas/EN_ESPERA')
        else:
            flash('Error al actualizar la cita: ' + str(data), 'error')
            return redirect(request.referrer)
    except requests.exceptions.RequestException as e:
        flash(f'Error de conexión: {str(e)}', 'error')
        return redirect(request.referrer)
    

@citas_view.route('/citas/delete/', methods=['POST'])
def delete_cita():
    codigo_cita = request.form['codigo_cita']
    r = requests.delete(f'http://localhost:5000/bd/citas/delete', data=json.dumps({'codigo_cita': codigo_cita}), headers={'Content-Type': 'application/json'})
    data = r.json().get('data')
    if r.status_code == 200:
        flash('Cita eliminada correctamente', 'success')
        return redirect('/citas/EN_ESPERA')
    else:
        flash('Error al eliminar la cita: ' + str(data), 'error')
        return redirect(request.referrer)

