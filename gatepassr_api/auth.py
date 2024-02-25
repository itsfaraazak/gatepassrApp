from flask import (
    Flask, jsonify, request, redirect, Blueprint
)

from gatepassr_api.database import data
from werkzeug.security import generate_password_hash, check_password_hash

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route("/requestregistration", methods = ["GET","POST"])
def process_sign_up():
    form_data = {
        "email": request.form["email"],
        "passwd": request.form["password"],
        "username":request.form["username"],
    }
    print("Registration - form data recieved")
    print(f"email is {form_data['email']} and password is {form_data['passwd']}")
    
    try:
        passwordhash = generate_password_hash(form_data['passwd'], method='pbkdf2:sha256')
        print(passwordhash)
        query =f"CALL register_user('{form_data['username']}', '{passwordhash}', '{form_data['email']}');"
        print(query)
        data.query_db(query, True)
        return redirect("http://localhost:5173/request-a-gatepass")
    except Exception as error:
        print(error)
        return redirect("http://localhost:5173/sign-up")
    
    # logging


@bp.route("/signin", methods = ["GET","POST"])
def sign_in():
    form_data = {
        "email": request.form["email"],
        "passwd": request.form["password"]
    }
    print("Sign in - form data recieved")
    print(f"email is {form_data['email']} and password is {form_data['passwd']}")
    try:
        passwordhash = generate_password_hash(form_data['passwd'], method='sha256')
        query =f"CALL check_user('{form_data['email']}', '{passwordhash}');"
        data.query_db(query, True)
        return redirect("http://localhost:5173/request-a-gatepass")
    except:
        return redirect("http://localhost:5173/sign-in")
    



def registeruser(username,email,passwordhash):
    query =f"CALL register_user('{username}','{email}', '{passwordhash}');"
    print(query)
    data.query_db(query, True)
    return True


    
        

