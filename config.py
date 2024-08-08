from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///logs.db'
db = SQLAlchemy(app)

# Lista de API keys válidas
API_KEYS = [
    "api_key_servicio1",
    "api_key_servicio2",
    "api_key_servicio3"
]
