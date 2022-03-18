from flask import Blueprint
from controllers.professionalController import getAll, create, getProfessionalBySpeciality, addPatientToProfessional, update, delete


professional_bp = Blueprint('professional_bp', __name__)
professional_bp.route('/', methods=['GET'])(getAll)
professional_bp.route('/', methods=['POST'])(create)
professional_bp.route('/find', methods=['GET'])(getProfessionalBySpeciality)
professional_bp.route('/add/<professional_id>', methods=['GET'])(addPatientToProfessional)


professional_bp.route('/<int:professional_id>/edit', methods=['POST'])(update)
professional_bp.route('/<int:professional_id>', methods=['DELETE'])(delete)