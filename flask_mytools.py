from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

def create_subapp_info():
    app_infos = []
    from shadowlist import subapp as shadowscrapy_blueprint
    app_infos.append((shadowscrapy_blueprint, '/ss'))
    return app_infos

_app_infos = create_subapp_info()

def create_db(app):
    app.config.from_object('app_config')
    db = SQLAlchemy(app)
    return db

def create_app(debug=False):
    """Create an application."""
    app = Flask(__name__)
    app.debug = debug
    app.config['SECRET_KEY'] = 'gjr39dkjn344_!67#'

    for bp, url_prefix in _app_infos:
        app.register_blueprint(bp, url_prefix=url_prefix)

    return app

if __name__ == '__main__':
    app = create_app(True)
else:
    app = create_app()

# db = create_db(app)

@app.route('/')
def hello_world():
    return 'This a web tools just for me.....'


if __name__ == '__main__':
    app.run()
