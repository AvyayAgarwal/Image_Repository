from flask import Blueprint, request, flash
import os

from . import db

bp = Blueprint('images', __name__, url_prefix='/images')

@bp.route('/', methods=["GET"])
def display():
    data = request.get_json()
    print('display - data', data)
    return 'display'


@bp.route('/upload', methods=["POST"])
def upload():
    data = request.get_json()
    if data is None:
        return 400
    
    db = get_db()
    print('upload - data', data)
    return 'upload'


@bp.route('/delete', methods=["POST"])
def delete():
    data = request.get_json()
    print('delete - data', data)
    return 'delete'
