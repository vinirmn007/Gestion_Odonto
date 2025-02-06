from flask import Blueprint, json, render_template, request, redirect, url_for, flash

login_view = Blueprint('login_view', __name__)

@login_view.route('/home')
def home():
    return 'Hola mundo'