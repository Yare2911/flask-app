from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ["DATABASE_URL"]

db = SQLAlchemy(app)    


from application import routes

