from flask import Blueprint, json, render_template, request, redirect, flash, url_for
import requests

receta_view = Blueprint('receta_view', __name__)

@receta_view.route('/receta/all')
def receta():
    r = requests.get('http://localhost:5000/bd/receta/all')
    data = r.json().get('data')
    if r.status_code == 200:
        return render_template('parts/receta/receta.html', recetas=data)
    else:
        flash('Error al cargar las recetas: ' + str(data), 'error')
        return redirect(request.referrer)

@receta_view.route('/receta/registro')
def registro_receta():
    return render_template('parts/receta/registro_receta.html')

@receta_view.route('/receta/registro/save', methods=['POST'])
def save_receta():
    dosis = request.form.get('dosis')
    medicamento = request.form.get('medicamento')
    cod_diagnostico = request.form.get('cod_diagnostico')
    print(dosis, medicamento, cod_diagnostico)

    r = requests.get(f'http://localhost:5000/bd/diagnostico/{cod_diagnostico}')
    print(r.json())
    if r.status_code != 200:
        flash('El código de diagnóstico no es válido. Asegúrate de que exista.', 'error')
        return redirect(request.referrer)
    
    headers = {'Content-Type': 'application/json'}
    data = {
        'dosis': dosis,
        'medicamento': medicamento,
        'cod_diagnostico': cod_diagnostico,
    }
    r = requests.post('http://localhost:5000/bd/receta/save', data=json.dumps(data), headers=headers)
    data = r.json().get('data')
    if r.status_code == 200:
        flash('Receta registrada correctamente', 'success')
        return redirect('/receta/all')
    else:
        flash('Error al registrar receta: ' + str(data), 'error')
        return redirect(request.referrer)

@receta_view.route('/receta/eliminar', methods=['POST'])
def eliminar_receta():
    codigo_receta = request.form.get('codigo_receta')
    r = requests.delete('http://localhost:5000/bd/receta/delete', data=json.dumps({'codigo_receta': codigo_receta}), headers={'Content-Type': 'application/json'})
    data = r.json().get('data')
    if r.status_code == 200:
        flash('Receta eliminada correctamente', 'success')
        return redirect(url_for('receta_view.receta'))
    else:
        flash('Error al eliminar receta: ' + str(data), 'error')
        return redirect(request.referrer)

@receta_view.route('/receta/update', methods=['POST'])
def editar_receta():
    headers = {'Content-Type': 'application/json'}
    data = {
        'codigo_receta': request.form.get('codigo_receta'),
        'dosis': request.form.get('dosis'),
        'medicamento': request.form.get('medicamento'),
        'cod_diagnostico': request.form.get('cod_diagnostico')
    }
    r = requests.put('http://localhost:5000/bd/receta/update', data=json.dumps(data), headers=headers)
    data = r.json().get('data')
    if r.status_code == 200:
        flash('Receta actualizada correctamente', 'success')
        return redirect('/receta/all')
    else:
        flash('Error al actualizar receta: ' + str(data), 'error')
        return redirect(request.referrer)

@receta_view.route('/receta/<int:codigo_receta>')
def ver_receta(codigo_receta):
    r = requests.get(f'http://localhost:5000/bd/receta/{codigo_receta}')
    data = r.json().get('data')
    return render_template('parts/receta/detalle_receta.html', receta=data)
