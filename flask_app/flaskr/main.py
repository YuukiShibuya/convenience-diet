from flaskr import app
from flask import render_template
import sqlite3
# from flask_sqlalchemy import SQLAlchemy
# app = Flask(__name__)

@app.route('/')
def index():
    # return "hello world"
    return render_template('index.html')

# @app.route('/result')
# def result():


