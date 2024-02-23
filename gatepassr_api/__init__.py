import os

from flask import Flask, session, redirect, render_template, request, url_for

import identity
import identity.web
import requests

from flask_session import Session

from . import config

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        # DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_object(config)
        Session(app)

        auth = identity.web.Auth(
            session=session,
            authority=app.config["AUTHORITY"],
            client_id=app.config["CLIENT_ID"],
            client_credential=app.config["CLIENT_SECRET"]
        )

    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'
    
    from . import get_data
    from . import post_data
    from . import auth
    app.register_blueprint(get_data.bp)
    app.register_blueprint(post_data.bp)
    app.register_blueprint(auth.bp)

    return app
