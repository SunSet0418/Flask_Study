from flask import Blueprint

blueprint = Blueprint('auth', __name__)

@blueprint.route('/login')
def login():
    return "LOGIN"
