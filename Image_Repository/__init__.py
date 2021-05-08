import os
from flask import Flask, render_template

from . import db, images


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
    
    app.config['UPLOAD_DIR'] = os.path.join(app.instance_path, 'uploads')
    os.makedirs(app.config['UPLOAD_DIR'], exist_ok=True)

    # a simple page that says hello
    @app.route('/')
    def health():
        return render_template('index.html')

    db.init_app(app)
    
    app.register_blueprint(images.bp)

    return app