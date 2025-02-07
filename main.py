from flask import Flask
from config import app

#Rutas de controladores
from controller.users_con import user_controller
from controller.roles_con import roles_controller
from controller.historialMedico_con import  historialMedico_controller

#Rutas de vistas
from views.users_view import user_view
<<<<<<< HEAD
from views.HistorialMedico_view import historialMedico_view
=======
from views.roles_view import roles_view
>>>>>>> origin/main

app.register_blueprint(user_controller)
app.register_blueprint(roles_controller)
app.register_blueprint(historialMedico_controller)
app.register_blueprint(user_view)
<<<<<<< HEAD
app.register_blueprint(historialMedico_view)
=======
app.register_blueprint(roles_view)

>>>>>>> origin/main
if __name__ == '__main__':
    app.secret_key = 'key-gestion-ondontonenas'
    app.config['SESSION_TYPE'] = 'filesystem'
    app.run(debug=True, host='0.0.0.0')
