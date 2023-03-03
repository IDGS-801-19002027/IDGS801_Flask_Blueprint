from flask import Blueprint

alumnos = Blueprint('alumnos', __name__)

@alumnos.route('/getalumno', methods=['GET'])
def getalumno():
    return {'key':'Alumnos' }