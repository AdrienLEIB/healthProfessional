from flask import Blueprint
from controllers.professionalController import index, create,store, show, update, delete


professional_bp = Blueprint('professional_bp', __name__)
professional_bp.route('/', methods=['GET'])(index)
professional_bp.route('/', methods=['POST'])(create)
professional_bp.route('/create', methods=['POST'])(store)
professional_bp.route('/<int:professional_id>', methods=['GET'])(show)
professional_bp.route('/<int:professional_id>/edit', methods=['POST'])(update)
professional_bp.route('/<int:professional_id>', methods=['DELETE'])(delete)