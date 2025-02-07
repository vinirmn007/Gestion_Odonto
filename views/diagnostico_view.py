from flask import Blueprint, json, render_template, request, redirect, flash, session, url_for
import requests

diagnostico_view = Blueprint('diagnostico_view', __name__)

@diagnostico_view.route('/diagnostico/all')
def diagnostico():
    r = requests.get('http://localhost:5000/bd/diagnostico/all')
    data = r.json().get('data')
    if r.status_code == 200:
        return render_template('parts/diagnostico/diagnostico.html', diagnosticos=data)
    else:
        flash('Error al cargar los diagnosticos', + str(data), 'error')
        return redirect(request.referrer)

@diagnostico_view.route('/diagnostico/registro')
def registro_diagnostico():
    return render_template('parts/diagnostico/registro_diagnostico.html')

@diagnostico_view.route('/diagnostico/registro/save', methods=['POST'])
def save_diagnostico():
    descripcion = request.form.get('descripcion')
    examen = request.form.get('examen')
    cod_cita = request.form.get('cod_cita')
    headers = {'Content-Type': 'application/json'}
    data = {
        'descripcion': descripcion,
        'examen': examen,
        'cod_cita': cod_cita,
    }
    r = requests.post('http://localhost:5000/bd/diagnostico/save', data=json.dumps(data), headers=headers)
    data = r.json().get('data')
    if r.status_code == 200:
        flash('Diagnostico registrado correctamente', 'success')
        return redirect('/diagnostico')
    else:
        flash('Error al registrar diagnostico' + str(data), 'error')
        return redirect(request.referrer)
    
@diagnostico_view.route('/diagnostico/eliminar', methods=['POST'])
def eliminar_diagnostico():
    codigo_diagnostico = request.form('codigo_diagnostico')
    r = requests.delete(f'http://localhost:5000/bd/diagnostico/delete', data=json.dumps({'codigo_diagnostico': codigo_diagnostico}), headers={'Content-Type': 'application/json'})
    data = r.json().get('data')
    if r.status_code == 200:
        flash('Diagnostico eliminado correctamente', 'success')
        return redirect(url_for('diagnostico_view.diagnostico'))
    else:
        flash('Error al eliminar diagnostico', + str(data), 'error')
        return redirect(request.referrer)

@diagnostico_view.route('/diagnostico/update/', methods=['POST'])
def editar_diagnostico():
    headers = {'Content-Type': 'application/json'}
    data = {
        'codigo_diagnostico': request.form.get('codigo_diagnostico'),
        'descripcion': request.form.get('descripcion'),
        'examen': request.form.get('examen'),
        'cod_cita': request.form.get('cod_cita')
    }
    r = requests.put('http://localhost:5000/bd/diagnostico/update', data=json.dumps(data), headers=headers)
    data = r.json().get('data')
    if r.status_code == 200:
        flash('Diagnostico actualizado correctamente', 'success')
        return redirect('/diagnostico/all')
    else:
        flash('Error al actualizar diagnostico', + str(data), 'error')
        return redirect(request.referrer)
    
@diagnostico_view.route('/diagnostico/<int:codigo_diagnostico>')
def ver_diagnostico(codigo_diagnostico):
    r = requests.get(f'http://localhost:5000/bd/diagnostico/{codigo_diagnostico}')
    data = r.json().get('data')
    return render_template('parts/diagnostico/detalle_diagnostico.html', diagnostico=data)



