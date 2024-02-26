import os

from flask import Flask, session, redirect, render_template, request, url_for

import identity
import identity.web
import requests

from flask_session import Session
#from flask_login import LoginManager

from . import config
auth_test:any

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_pyfile('config.py')
    print(app.config)
    #app.config.from_mapping(
        #SECRET_KEY='dev',
        # DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
   #)
    """login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)
    

    if test_config is None:
        # config for authentication
        # load the instance config, if it exists, when not testing
        
        app.config.from_object(config)
        assert app.config["REDIRECT_PATH"] != "/", "REDIRECT_PATH must not be /"
        Session(app)

        # This section is needed for url_for("foo", _external=True) to automatically
        # generate http scheme when this sample is running on localhost,
        # and to generate https scheme when it is deployed behind reversed proxy.
        # See also https://flask.palletsprojects.com/en/2.2.x/deploying/proxy_fix/
        from werkzeug.middleware.proxy_fix import ProxyFix
        app.wsgi_app = ProxyFix(app.wsgi_app, x_proto=1, x_host=1)

        app.jinja_env.globals.update(Auth=identity.web.Auth)  # Useful in template for B2C
        auth = identity.web.Auth(
            session=session,
            authority=app.config["AUTHORITY"],
            client_id=app.config["CLIENT_ID"],
            client_credential=app.config["CLIENT_SECRET"],
        )
        auth_test = auth
        
        app.config.from_pyfile('config.py')
    else:
        # load the test config if passed in
        #app.config.from_mapping(test_config)
        pass # for now again...
        """

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from . import get_data
    from . import post_data
    from . import auth
    app.register_blueprint(get_data.bp)
    app.register_blueprint(post_data.bp)
    app.register_blueprint(auth.bp)
    #with app.app_context():
    #    app.register_blueprint(auth.bp)
    
    #@login_manager.user_loader
    #def load_user(user_id):
        # since the user_id is just the primary key of our user table, use it in the query for the user
        #return getuser(int(user_id))
    

    return app
