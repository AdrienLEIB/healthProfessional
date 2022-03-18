import sys
from flask import render_template, redirect, url_for, request, abort, jsonify
from models.Professional import Professional
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

def index():
    return jsonify({"id": 2})

def create():
    newPro = Professional("Adrien", "Medecin Du SPort", 4, 5, )
    db.session.add(newPro)
    db.session.commit()
    return "Succes"

def store():
    return  "tata"
def show(professionalID):
    return "titi"
def update(professionalID):
    return "toto"
def delete(professionalID):
    return "it"