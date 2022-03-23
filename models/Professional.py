from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import UUID
db = SQLAlchemy()
import uuid




patients = db.Table('patients_follow',
    db.Column('patient_id',  db.Text(length=36), db.ForeignKey('patient.id')),
    db.Column('professional_id', db.Text(length=36), db.ForeignKey('professional.id'))
)


class Professional(db.Model):
    __tablename__ = 'professional'
    id = db.Column('id', db.Text(length=36), default=lambda: str(uuid.uuid4()), primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    speciality= db.Column(db.String(80), nullable=False)
    longitude= db.Column(db.Integer, primary_key=True)
    latitute= db.Column(db.Integer, primary_key=True)
    patients = db.relationship("Patient", secondary=patients)

    def __repr__(self):
        return '<Patient %r>' % self.name

    @property
    def serialize(self):
        """Return object data in easily serializable format"""
        return {
            'id': self.id,
            'name':self.name,
            'speciality': self.speciality,
            'longitude': self.longitude,
            'latitude': self.latitute,
        }


class Patient(db.Model):
    __tablename__ = 'patient'
    id = db.Column('id', db.Text(length=36), default=lambda: str(uuid.uuid4()), primary_key=True)



