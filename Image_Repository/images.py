from flask import Blueprint, request, flash, current_app, render_template, redirect, g
import os
from werkzeug.utils import secure_filename
import time

from Image_Repository.db import get_db
from Image_Repository.auth import login_required

bp = Blueprint('images', __name__, url_prefix='/images')


@bp.route("/")
def index():
    return render_template("repository/index.html")


@bp.route('/display', methods=["GET"])
def display():
    try:
        db = get_db()
        user = g.user["id"] if g.user else 0

        if user > 0:
            data = db.execute('SELECT * FROM images WHERE author_id = 0 OR author_id = ?', (user, )).fetchall()
        else:
            data = db.execute('SELECT * FROM images WHERE author_id = 0').fetchall()

        images = [row[-1] for row in data]
        if len(images) <= 0:
            flash("No images to display")
            return redirect('/images')
        return render_template("repository/images.html", images=images)

    except Exception as e:
        flash(f'Error in fetching image(s): {e}')
        return render_template("repository/index.html")


@bp.route('/upload', methods=["POST"])
def upload():
    try:
        db = get_db()
        filenames = []

        public_flag = True if request.form.get('ispublic') else False
        user = g.user["id"] if g.user else 0

        if not public_flag and not user:
            flash(f'Please log in to upload privately')
            return render_template("repository/index.html")

        for file in request.files.getlist('file'):
            name = secure_filename(str(int(time.time())) + '_' + file.filename)
            filenames.append((user, public_flag, name))
            file.save(os.path.join(current_app.config['UPLOAD_DIR'], name))

        db.executemany('INSERT INTO images (author_id, public, image) VALUES (?, ?, ?)', filenames)
        db.commit()
        return redirect('/images/display')

    except Exception as e:
        flash(f'Error in uploading image(s): {e}')
        return render_template("repository/index.html")


@bp.route('/delete', methods=["POST"])
@login_required
def delete():
    try:
        db = get_db()
        images = [(image,) for image in request.form]
        
        db.executemany('DELETE FROM images WHERE image = ?', images)
        for image in request.form:
            os.remove(os.path.join(current_app.config['UPLOAD_DIR'], image))
        
        db.commit()
        return redirect('/images/display')

    except Exception as e:
        flash(f'Error in deleting image(s): {e}')
        return render_template("repository/index.html")
