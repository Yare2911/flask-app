from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = "postgres://jhyoqfgs:f66Q4WOw4sogdhg7J1sTaSdP6p_uVTHQ@trumpet.db.elephantsql.com/jhyoqfgs"
db = SQLAlchemy(app)    


from application import routes

