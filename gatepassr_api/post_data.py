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
        data.query_db(query, True)
        print(form_data)
        return redirect("http://localhost:5173")
    except:
        print(query)
        print(form_data)
        return redirect("http://localhost:5173/request-a-gatepass")
