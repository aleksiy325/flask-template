from flask import Flask
from flask import url_for
from flask import render_template
from werkzeug.routing import BaseConverter
from models.models import User, db 
import requests

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = ''
app.app_context().push()
db.init_app(app)

test = User('test', 'test')

@app.route("/")
def hello():
   	return render_template('pages/home.html', title='home')

@app.route("/something")
def something():
	return "Something else!"

if __name__ == "__main__":
    app.run()