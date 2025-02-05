from flask import Flask
from models import db, Car

app = Flask(__name__)

host = 'localhost'
port = '5432'
user = 'postgres'
password = 'password'
database = 'flask'

app.secret_key = 'SecretApp'

app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{user}:{password}@{host}:{port}/{database}'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

