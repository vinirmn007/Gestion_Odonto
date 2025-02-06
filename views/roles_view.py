from flask import Blueprint, json, render_template, request, redirect, flash, session
import requests

roles_view = Blueprint('roles_view', __name__)