from flask import Blueprint, request, flash, current_app
import os
from werkzeug.utils import secure_filename
import time

from Image_Repository.db import get_db

bp = Blueprint('images', __name__, url_prefix='/images')

@bp.route('/', methods=["GET"])
def display():
    data = request.get_json()
    print('display - data', request.args, data)

    return 'display'


@bp.route('/upload', methods=["POST"])
def upload():
    try:
        d = get_db()
        filenames = []

        for file in request.files.getlist('file'):
            name = secure_filename(str(int(time.time())) + '_' + file.filename)
            filenames.append((file.filename, name))
            file.save(os.path.join(os.path.join(current_app.config['UPLOAD_DIR'], name)))
        
        d.executemany('INSERT INTO images (title, image) VALUES (?, ?)', filenames)
        d.commit()
        return 'File uploaded successfully!'

    except Exception as e:
        return f'Error in uploading image(s): {e}', 400


@bp.route('/delete', methods=["POST"])
def delete():
    data = request.get_json()
    print('delete - data', data)

    return 'delete'
