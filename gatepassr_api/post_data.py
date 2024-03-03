import json
from flask import (
    Flask, jsonify, request, redirect, Blueprint
)

from gatepassr_api.database import data

bp = Blueprint('post_data', __name__, url_prefix='/submit')

@bp.route("/gatepassrequest", methods = ["POST"])
def sumbit_request():
    form_data = {
        "student_type": request.form["student_type"],
        "grade": request.form["grade"],
        "exit_time": request.form["exit-time"],
        "guardian_name": request.form["name-guardian"],
        "guardian_relation": request.form["guardian-relation"],
        "guardian_email": request.form["email"],
        "reason_for_gatepass": request.form["about"]
    }
    query = f"""CALL insert_data('Yassss', 'studentEmail@example.com', '{form_data["grade"]}', {int(form_data["student_type"])}, '{form_data["exit_time"]}', '{form_data["guardian_name"]}', '{form_data['guardian_relation']}', '{form_data['guardian_email']}', '{form_data['reason_for_gatepass']}');"""
# update stored procedure for processing guardian details and email + reason
    try:
        print(query)
        #data.query_db(query, True)
        data.commandquery(query)
        print(form_data)
        return redirect("http://localhost:5173")
    except:
        print(query)
        print(form_data)
        return redirect("http://localhost:5173/request-a-gatepass")

@bp.route("/approverequest", methods=["POST"])
def approve_gatepass_request():
    print("test")
    #print(request.form['btnapprove'])
    content_type = request.headers.get('Content-Type')
    print(content_type)
    if (content_type == 'application/json'):
        req = request.json
        print(req)
    else:
        print('Json Content-Type not supported!')
        #requestid = (request.data)
        requestid = int(request.data.decode("utf-8"))
        print(requestid)
    try:
        #query = "UPDATE requests SET approved_by = 'teacher@example.com', approved_at = NOW() WHERE request_id = 3;"
        query=f"""CALL approve_request({requestid},'teacher@abc.com');"""
        print(query)
        data.commandquery(query)
        print("ok")
        return "success"
    except Exception as e:
        print(f"Error: {e}")
        return "try again"
    
