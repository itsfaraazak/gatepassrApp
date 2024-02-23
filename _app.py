from flask import Flask, jsonify, request, redirect
import logging

import sys
sys.path.insert(0, "database")

from database import data

app = Flask(__name__)

@app.route("/")
def hello_world():
    request = jsonify(data.get_request())
    # print(request)
    request.headers.add("Access-Control-Allow-Origin", "*")
    return request

@app.route("/submitrequest", methods = ["POST"])
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

    try:
        data.insert_request_data(form_data)
        print(form_data)
        return redirect("http://localhost:5173")
    except:
        print(form_data)
        return redirect("http://localhost:5173/request-a-gatepass")


@app.route("/getrequests", methods = ["GET"])
def requests():
    request = jsonify(data.get_data(data.query_requests))
    request.headers.add("Access-Control-Allow-Origin", "*")
    return request

@app.route("/getgrades", methods = ["GET"])
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
    request = jsonify(grades)
    request.headers.add("Access-Control-Allow-Origin", "*")
    return request
    


if __name__ == '__main__':
    app.run()
