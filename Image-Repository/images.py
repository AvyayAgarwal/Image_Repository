from flask import Blueprint, request, flash, current_app
import os

from . import db

bp = Blueprint('images', __name__, url_prefix='/images')

@bp.route('/', methods=["GET"])
def display():
    data = request.get_json()
    print('display - data', request.args, data)

    return 'display'


@bp.route('/upload', methods=["POST"])
def upload():
    data = request.get_json()

    for file in request.files.getlist('file'):
        file.save(os.path.join(os.path.join(current_app.config['UPLOAD_DIR'], file.filename)))
    
    return 'upload'


@bp.route('/delete', methods=["POST"])
def delete():
    data = request.get_json()
    print('delete - data', data)

    return 'delete'
