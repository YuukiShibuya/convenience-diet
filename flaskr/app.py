from re import I
from flask import Flask
# from flaskr import app
from flask import render_template
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

@app.route('/')
def index():
    # return "hello world"
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)