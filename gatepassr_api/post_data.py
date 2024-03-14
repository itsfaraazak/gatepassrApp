import json
from flask import (
    Flask, jsonify, request, redirect, Blueprint
)
from flask import current_app

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
        return redirect(current_app.config['FRONTEND_URL'])
            #"http://localhost:5173")
    except:
        print(query)
        print(form_data)
        return redirect(current_app.config['FRONTEND_URL'] +"/request-a-gatepass")

@bp.route("/approverequest", methods=["POST"])
def approve_gatepass_request():
    content_type = request.headers.get('Content-Type')
    print(content_type)
    if (content_type == 'application/json'):
        req = request.json
        print(req)
    else:
        print('Json Content-Type not supported!')
        requestid = int(request.data.decode("utf-8"))
        print(requestid)
    try:
        #query = "UPDATE requests SET approved_by = 'teacher@example.com', approved_at = NOW() WHERE request_id = 3;"
        query=f"""CALL approve_request({requestid},'teacher@abc.com');"""
        data.commandquery(query)
        return "success"
    except Exception as e:
        print(f"Error: {e}")
        return "try again"

@bp.route("/profiledata", methods=["POST"])   
def submit_profile():
    print("Profile")
    #try:
    """     data = request.data
    print(data)
    """
    profile_data = json.loads(request.data)
    print(profile_data)
    print(type(profile_data))
    
    #update two tables
    
    query = f"""CALL profiledata('{profile_data["primary_guardian_name"]}','{profile_data["primary_contact_number"]}','{profile_data["secondary_guardian_name"]}','{profile_data["secondary_contact_number"]}','testing@abc.com')"""
    print(query)
    data.commandquery(query)
    return("Profile saved")
    #except:
    #    return("Please try again.")
    
