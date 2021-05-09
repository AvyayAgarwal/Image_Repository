import os
from flask import Flask, render_template, redirect

from . import db, images, auth


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'Image_Repository.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    
    app.config['UPLOAD_DIR'] = os.path.join('Image_Repository', 'static')
    os.makedirs(app.config['UPLOAD_DIR'], exist_ok=True)

    @app.route("/health")
    def health():
        return "Green"

    @app.route('/')
    def hello():
        return redirect('/images')

    db.init_app(app)
    
    app.register_blueprint(auth.bp)
    app.register_blueprint(images.bp)

    app.add_url_rule("/images", endpoint="index")

    return app