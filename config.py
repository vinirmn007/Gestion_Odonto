from flask import Flask
from flask_mysqldb import MySQL

app = Flask(__name__)

# Configuración de la base
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'admin_base'
app.config['MYSQL_PASSWORD'] = 'Admin.123'
app.config['MYSQL_DB'] = 'Proyecto_Final'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql = MySQL(app)