from flask import Flask
from config import app

#Rutas de controladores
from controller.users_con import user_controller
from controller.roles_con import roles_controller
from controller.historialMedico_con import  historialMedico_controller
from controller.diagnostico_con import diagnostico_controller
from controller.receta_con import receta_controller
from controller.citas_con import citas_controller
from controller.ondontologo_con import odon_controller

#Rutas de vistas
from views.users_view import user_view
from views.HistorialMedico_view import historialMedico_view
from views.roles_view import roles_view
from views.diagnostico_view import diagnostico_view
from views.receta_view import receta_view
from views.ondontologo_view import odonto_view

#Rutas de vistas
from views.users_view import user_view
from views.citas_view import citas_view

app.register_blueprint(user_controller)
app.register_blueprint(roles_controller)
app.register_blueprint(historialMedico_controller)
app.register_blueprint(diagnostico_controller)
app.register_blueprint(user_view)
app.register_blueprint(historialMedico_view)
app.register_blueprint(roles_view)
app.register_blueprint(diagnostico_view)
app.register_blueprint(receta_view)
app.register_blueprint(receta_controller)
app.register_blueprint(citas_controller)
app.register_blueprint(citas_view)
app.register_blueprint(odon_controller)
app.register_blueprint(odonto_view)

if __name__ == '__main__':
    app.secret_key = 'key-gestion-ondontonenas'
    app.config['SESSION_TYPE'] = 'filesystem'
    app.run(debug=True, host='0.0.0.0')
