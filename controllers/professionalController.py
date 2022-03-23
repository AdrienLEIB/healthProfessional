import sys
from flask import render_template, redirect, url_for, request, abort, jsonify
from models.Professional import Professional, Patient
from flask_sqlalchemy import SQLAlchemy
import uuid

db = SQLAlchemy()

def getAll():
    return jsonify([i.serialize for i in Professional.query.all()]) 


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


def getProfessionalBySpeciality():

    speciality = request.args.get('speciality') if  request.args.get('speciality') else "*"
    latitude  = request.args.get('latitude') if request.args.get('latitude') else "*"
    longitude = request.args.get('longitude') if request.args.get('longitude') else "*"
    try:
        qry = Professional.query.filter(Professional.latitute.between(int(latitude)-2, int(latitude)+2)).filter(Professional.longitude.between(int(longitude)-2, int(longitude)+2)).filter_by(speciality=speciality) if type(latitude)==int and type(longitude)==int else Professional.query.filter_by(speciality=speciality)
        results = [
            {
                "id": pro.id,
                "name": pro.name,
                "speciality": pro.speciality,
                "longitude": pro.longitude,
                "latitute": pro.latitute,

            } for pro in qry]

        return jsonify(results)
    except:
        return "400"


def addPatientToProfessional(professional_id):
    patient = request.form['patient'] if request.form['patient'] else None
    try:
        qry = Professional.query.filter_by(id=professional_id).join(Patient, Patient.id == patient)
        if qry.count()>0:
            return "Le patient est déjà inscrit"

        qryPatient = Patient.query.filter_by(id=patient).first()

        if qryPatient is None:
            newPatient = Patient(id=patient)
            db.session.add(newPatient)

        qryPatient = Patient.query.filter_by(id=patient).first()
        queue = Professional.query.filter_by(id=professional_id).first()
        queue.patients.append(qryPatient)
        db.session.commit()
        return "201"

    except Exception as e:
        return f"<h1>{professional_id}, {patient}, {e}</h1>"


def update(professionalID):
    return "update in progress"
def delete(professionalID):
    return "delete in progress"