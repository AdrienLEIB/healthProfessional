import sys
from flask import render_template, redirect, url_for, request, abort, jsonify
from models.Professional import Professional
from flask_sqlalchemy import SQLAlchemy
import uuid

db = SQLAlchemy()

def getAll():
    pros = Professional.query.all()
    results = [
        {
            "name": pro.name,
            "speciality": pro.speciality,
            "longitude": pro.longitude,
            "latitute": pro.latitute,

        } for pro in pros]

    return jsonify(results)


def create():

    try:
        name = request.form['name'] if request.form['name'] else None
        speciality = request.form['speciality'] if request.form['speciality'] else None
        latitute = request.form['latitute'] if request.form['latitute'] else None
        longitude = request.form['longitude'] if request.form['longitude'] else None
        admin = Professional( name=name, speciality=speciality, latitute=latitute, longitude=longitude)
        db.session.add(admin)
        db.session.commit()
        return "201"
    except:
        return "400"


def show(professionalID):
    return "titi"

def getProfessionalBySpeciality(professionalSpeciality):
    try:
        speciality = professionalSpeciality if professionalSpeciality else None
        pros = Professional.query.filter(Professional.speciality(speciality))
        results = [
            {
                "id": pro.id,
                "name": pro.name,
                "speciality": pro.speciality,
                "longitude": pro.longitude,
                "latitute": pro.latitute,

            } for pro in pros]

        return jsonify(results)
    except:
        return "400"

def update(professionalID):
    return "toto"
def delete(professionalID):
    return "it"