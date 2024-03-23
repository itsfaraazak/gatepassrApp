from flask import (
    Flask, jsonify, request, redirect, Blueprint
)

from gatepassr_api.database import data
import json

bp = Blueprint('get_data', __name__, url_prefix='/recieve')

@bp.route("/studenttype")
def student_type():
    return send_request(data.query_db("SELECT student_type_id, student_type FROM student_type;"))
    #request = jsonify(data.query_db("SELECT student_type_id, student_type FROM student_type;"))
    # print(request)
    #request.headers.add("Access-Control-Allow-Origin", "*")
    #return request

@bp.route("/allrequests", methods = ["GET"])
def requests():
    query_requests = """SELECT req.student_name, 
    req.student_email, 
    student_grade, 
    req.student_type_id,
    exit_time,
    st_type.student_type,
    approved_by,
    req.request_id
FROM requests req
join public.student_type st_type
on req.student_type_id = st_type.student_type_id"""
    return send_request(data.query_db(query_requests))
    #request = jsonify(data.query_db(query_requests))
    #request.headers.add("Access-Control-Allow-Origin", "*")
    #return request


@bp.route("/pendingrequests", methods = ["GET"])
def request():
    query_requests = """SELECT req.student_name,
      req.student_email, 
      student_grade, 
      req.student_type_id, 
      exit_time,
    st_type.student_type,
    approved_by,
    req.request_id
FROM requests req
join public.student_type st_type
on req.student_type_id = st_type.student_type_id
WHERE approved_by IS NULL
AND exit_time >= DATE(now())
ORDER BY exit_time ASC;"""
    return send_request(data.query_db(query_requests))
    

@bp.route("/todaysrequests", methods = ["GET"])
def get_todays_requests():
    query = """SELECT stname, stgrade, approvedat,exittime FROM get_todays_requests();"""
    return send_request(data.query_db(query))


@bp.route("/grades", methods = ["GET"])
def get_grades():
    grades = {
        1: "PYP-1",
        2: "PYP-2",
        3: "PYP-3",
        4: "PYP-4",
        5: "PYP-5",
        6: "MYP-1",
        7: "MYP-2",
        8: "MYP-3",
        9: "MYP-4",
        10: "MYP-5",
        11: "DP-1",
        12: "DP-2"
    }
    return send_request(grades)

def send_request(data):
    request = jsonify(data)
    request.headers.add("Access-Control-Allow-Origin", "*")
    return request



