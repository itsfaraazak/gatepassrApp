import json
from flask import (
    Flask, jsonify, request, redirect, Blueprint, make_response
)

from gatepassr_api.database import data
from werkzeug.security import generate_password_hash, check_password_hash

from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask import current_app


bp = Blueprint('auth', __name__, url_prefix='/auth')
"""
sign up original
@bp.route("/requestregistration", methods = ["GET","POST"])
def process_sign_up():
    form_data = {
        "email": request.form["email"],
        "passwd": request.form["password"],
        "username":request.form["username"],
    }
    print("Registration - form data recieved")
    print(f"email is {form_data['email']} and password is {form_data['passwd']}")
    passwordhash = generate_password_hash(form_data['passwd'], method='pbkdf2:sha256', salt_length=8)
    #passwordhash =form_data['password']
    print(passwordhash)
    
    try:
        query =f"CALL register_user('{form_data['username']}', '{passwordhash}', '{form_data['email']}');"
        print(query)
        data.query_db(query, True)
        return redirect("http://localhost:5173/auth/request-a-gatepass")
    except Exception as error:
        print(error)
        return redirect("http://localhost:5173/auth/sign-up")
    

    
    # logging
"""

@bp.route("/requestregistration", methods = ["POST"])
def process_sign_up():
    print(request.data)

    # Decode the byte sequence to a string
    json_string = request.data.decode('utf-8')

    # Parse the JSON string
    sign_up_data = json.loads(json_string)

    # Now 'json_data' is a Python dictionary
    print(sign_up_data)
    print("Registration - form data recieved")
    print(f"email is {sign_up_data['email']} and password is {sign_up_data['password']}")
    passwordhash = generate_password_hash(sign_up_data['password'], method='pbkdf2:sha256', salt_length=8)
    #passwordhash =form_data['password']
    print("1st hash",passwordhash)
    passwordhash2 = generate_password_hash(sign_up_data['password'], method='pbkdf2:sha256', salt_length=8)
    print("2nd hash",passwordhash2)
    try:
        query =f"CALL register_user('{sign_up_data['username']}', '{passwordhash}', '{sign_up_data['email']}');"
        print(query)
        data.commandquery(query)
        return redirect(current_app.config['FRONTEND_URL']+"/auth/request-a-gatepass")
    except Exception as error:
        print(error)
        return redirect(current_app.config['FRONTEND_URL']+"/auth/sign-up")
    

    
    # logging

# original
""" @bp.route("/login", methods = ["GET","POST"])
def sign_in():
    form_data = {
        "email": request.form["email"],
        "passwd": request.form["password"]
    }
    print("Sign in - form data recieved")
    print(f"email is {form_data['email']} and password is {form_data['passwd']}")
    passwordhash = generate_password_hash(form_data['passwd'], method='pbkdf2:sha256', salt_length=8)
    print(passwordhash)

    try:
        query =f"CALL check_user('{form_data['email']}', '{passwordhash}');"
        data.query_db(query, True)
        access_token = create_access_token(identity=form_data["email"])
        print(access_token)
        return jsonify(access_token=access_token)
    
    except Exception as error:
        print(error)
        return jsonify({"msg": "Bad email or password"}), 401 """
    

@bp.route("/signin", methods = ["GET","POST"])
def sign_in():
    print(request.data)
    print("signin==========")
    # Decode the byte sequence to a string
    json_string = request.data.decode('utf-8')

    # Parse the JSON string
    sign_in_data = json.loads(json_string)

    # Now 'json_data' is a Python dictionary
    print(sign_in_data)

    #form_data = jsonify(str(request.data))
    #print(form_data)
    passwordhash = generate_password_hash(sign_in_data["password"], method='pbkdf2:sha256', salt_length=8)
    #passwordhash =sign_in_data["password"]
    print(passwordhash)

    try:
        #query =f"""CALL check_user('{passwordhash}','{sign_in_data["username"]}');"""
        query =f""" SELECT * FROM check_user('{sign_in_data["username"]}')"""
        print(query)
        result = data.query_db(query, True)
        print("result-----",result[1])
        isAuthorized = check_password_hash(result[1],sign_in_data["password"])
        if(isAuthorized):
            access_token = create_access_token(identity=sign_in_data["username"])
            response = make_response(jsonify({'access_token': access_token}))
            response.headers["Access-Control-Allow-Headers"] = "Authorization"
            print(response)
            return response
        else:
            return jsonify({"msg": "Incorrect email or password"}), 401
    except Exception as error:
        print(error)
        return jsonify({"msg": "Incorrect email or password"}), 401

    

@bp.route("/protected", methods=["GET"])
@jwt_required()
def protected():
    # Access the identity of the current user with get_jwt_identity
    print("ABCD")
    current_user = get_jwt_identity()
    print(current_user)
    return jsonify(logged_in_as=current_user), 200


def registeruser(username,email,passwordhash):
    query =f"CALL register_user('{username}','{email}', '{passwordhash}');"
    print(query)
    data.query_db(query, True)
    return True


    
        

