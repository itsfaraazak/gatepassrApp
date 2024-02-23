import identity
import identity.web
import requests
from flask import Flask, redirect, render_template, request, session, url_for
from flask_session import Session

from . import config

app = Flask(__name__, template_folder=".")
app.config.from_object(config)
Session(app)

auth = identity.web.Auth(
    session=session,
    #grant_type = password
    authority="https://login.microsoftonline.com/bdf2e8e8-a194-49a9-bfd5-2f158f6202ac",
    client_id="7c659433-56d2-447c-a0f0-cbb77e0c9090",
    client_credential="oHt8Q~z_.WXBsqHj1fr-FzMHQQ1XQ95JlcBsBaAT",
)

#@app.route("/")
#def index():
    #if not (app.config["CLIENT_ID"] and app.config["CLIENT_SECRET"]):
        # This check is not strictly necessary.
        # You can remove this check from your production code.
        #return render_template('config_error.html')
#    if not auth.get_user():
#        return redirect(url_for("login"))
#    return render_template('index.html', user=auth.get_user(), version=identity.__version__)

@app.route("/login")
def login():
    return render_template("login.html", version=identity.__version__, **auth.log_in(
        scopes=config.SCOPE, # Have user consent to scopes during log-in
        #redirect_uri=url_for("auth_response", _external=True), # Optional. If present, this absolute URL must match your app's redirect_uri registered in Azure Portal
        ))

@app.route("/localhost:3000/getAToken")
def auth_response():
    result = auth.complete_log_in(request.args)
    print(1)
    #if "error" in result:
        #return render_template("auth_error.html", result=result)
    return redirect("https://localhost:3000")

@app.route("/logout")
def logout():
    return redirect(auth.log_out("https://localhost:3000", _external=True))

