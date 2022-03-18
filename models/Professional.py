from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

patients = db.Table('patients',
    db.Column('patient_id', db.Integer, db.ForeignKey('patient.id'), primary_key=True),
    db.Column('professional_id', db.Integer, db.ForeignKey('professional.id'), primary_key=True)
)

class Professional(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    speciality= db.Column(db.String(80), unique=True, nullable=False)
    longitude= db.Column(db.Integer, primary_key=True)
    latitute= db.Column(db.Integer, primary_key=True)
    patients = db.relationship('Patient', secondary=patients, lazy='subquery',
        backref=db.backref('Profesionnal', lazy=True))

    def __init__(self, name,speciality, longitude, latitude, ):
        self.name = name
        self.speciality = speciality
        self.longitude = longitude
        self.latitude = latitude


class Patient(db.Model):
    id = db.Column(db.Integer, primary_key=True)


