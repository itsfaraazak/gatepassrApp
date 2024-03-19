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
        "student_list": request.form["student_list"],
        "exit_time": request.form["exit-time"],
        "guardian_name": request.form["name-guardian"],
        "guardian_relation": request.form["guardian-relation"],
        "guardian_email": request.form["email"],
        "reason_for_gatepass": request.form["about"]
    }
    studentdata = form_data["student_list"].split(",")
    query = f"""CALL insert_data('{studentdata[0]}', '{studentdata[1]}', '', {int(form_data["student_type"])}, '{form_data["exit_time"]}', '{form_data["guardian_name"]}', '{form_data['guardian_relation']}', '{form_data['guardian_email']}', '{form_data['reason_for_gatepass']}');"""

    #query = f"""CALL insert_data('Yassss', 'studentEmail@example.com', '{form_data["grade"]}', {int(form_data["student_type"])}, '{form_data["exit_time"]}', '{form_data["guardian_name"]}', '{form_data['guardian_relation']}', '{form_data['guardian_email']}', '{form_data['reason_for_gatepass']}');"""
# update stored procedure for processing guardian details and email + reason
    try:
        print(query)
        #data.query_db(query, True)
        data.commandquery(query)
        print(form_data)
        return redirect(current_app.config['FRONTEND_URL']+"/status-console")
            #"http://localhost:5173")
    except:
        print(query)
        print(form_data)
        return redirect(current_app.config['FRONTEND_URL'] +"/status-console")

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
   
    profile_data = json.loads(request.data)
    print(profile_data)

    jdata = json.dumps(profile_data["student_list"])
  
    #update two tables
    #query = f"""SELECT  * FROM profiledatafunction('{profile_data["guardian_id"]}','{profile_data["primary_guardian_email"]}','{profile_data["primary_contact_number"]}','{profile_data["secondary_guardian_email"]}','{profile_data["secondary_contact_number"]}','{profile_data["created_by"]}','{jdata}');"""
    if profile_data["guardian_id"] == 0:
       query = f"""CALL profiledata('{profile_data["primary_guardian_email"]}','{profile_data["primary_contact_number"]}','{profile_data["secondary_guardian_email"]}','{profile_data["secondary_contact_number"]}','{profile_data["created_by"]}','{jdata}')"""
       print(query)
    else:
        query = f"""CALL profiledataupdate('{profile_data["guardian_id"]}','{profile_data["primary_guardian_email"]}','{profile_data["primary_contact_number"]}','{profile_data["secondary_guardian_email"]}','{profile_data["secondary_contact_number"]}','{profile_data["created_by"]}','{jdata}')"""
      
    data.commandquery(query)
    return  "Profile saved"
    #except:
    #    return("Please try again.")
    

@bp.route("/isauthorized", methods=["POST"]) 
def isauthorized():
   print("isAuthorized")
   userdata =json.loads(request.data)
   useremail= userdata["user_email"]
   query = f"""
      SELECT teacher_id
        ,teacher_email
        ,student_type_id
        ,student_grade
        ,is_admin
        FROM public.approval_teachers
        WHERE teacher_email ='{useremail}'
        and is_admin =True
   """
   print(request.data)
   return send_request(data.query_db(query))
   return "test response"

@bp.route("/profile", methods = ["POST"])
def get_profile():
    #return {"guardian_id": 10, "primary_guardian_email": "itsyasmeenkhan@gmail.com", "secondary_guardian_email": "second@abc.com", "primary_contactnumber": "12345", "seconday_contactnumber": "789456123", "student_list": [{"grade": 6, "student_name": "first", "student_email": "first@abc.com"}]}
    #return {"guardian_id": "10"}
    userdata =json.loads(request.data)
    useremail= userdata["user_email"]
    print(useremail)
    query = f"""Select guardian_id, primary_guardian_email ,secondary_guardian_email,primary_contactnumber,seconday_contactnumber, student_list from guardian Where created_by='{useremail}' order by created_on  desc Limit 1;"""
    print(query)
   
    dbdata =data.getdata_Json(query)

    response = json.loads(json.dumps(dbdata))
    
    print(response)
    print(type(response))
    
    return send_request(response)
    
def send_request(data):
    request = jsonify(data)
    request.headers.add("Access-Control-Allow-Origin", "*")
    return request

@bp.route("/userrequests", methods = ["POST"])
def get_user_requests():
    userdata =json.loads(request.data)
    useremail= userdata["user_email"]
    query = f"""SELECT req.student_name,
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
    WHERE guardian_email='{useremail}' OR student_email='{useremail}'
    ORDER BY exit_time DESC;""" 
    return send_request(data.query_db(query))