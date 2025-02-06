from flask import Flask
from config import app

#Rutas de controladores
from controller.users_con import user_controller

#Rutas de vistas
from views.login_view import login_view

app.register_blueprint(user_controller)
app.register_blueprint(login_view)

if __name__ == '__main__':
    app.secret_key = 'key-gestion-ondontonenas'
    app.config['SESSION_TYPE'] = 'filesystem'
    app.run(debug=True, host='0.0.0.0')
