from flask import Blueprint, request, flash, current_app, render_template
import os
from werkzeug.utils import secure_filename
import time

from Image_Repository.db import get_db

bp = Blueprint('images', __name__, url_prefix='/images')

@bp.route('/', methods=["GET"])
def display():
    try:
        db = get_db()
        data = db.execute('SELECT * FROM images').fetchall()
        images = [row[-1] for row in data]
        if len(images) <= 0:
            return 'No images to display'
        return render_template("images.html", images=images)

    except Exception as e:
        return f'Error in fetching image(s): {e}', 400


@bp.route('/upload', methods=["POST"])
def upload():
    try:
        db = get_db()
        filenames = []

        for file in request.files.getlist('file'):
            name = secure_filename(str(int(time.time())) + '_' + file.filename)
            filenames.append((file.filename, name))
            file.save(os.path.join(current_app.config['UPLOAD_DIR'], name))

        db.executemany('INSERT INTO images (title, image) VALUES (?, ?)', filenames)
        db.commit()
        return 'File uploaded successfully!'

    except Exception as e:
        return f'Error in uploading image(s): {e}', 400


@bp.route('/delete/<image>', methods=["POST"])
def delete(image):
    try:
        db = get_db()
        data = db.execute('DELETE FROM images WHERE image = ?', (image,))
        
        os.remove(os.path.join(current_app.config['UPLOAD_DIR'], image))
        db.commit()

        return f'Image {image} delete successfully!'

    except Exception as e:
        return f'Error in deleting image {image}: {e}', 400
