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
        "student_count": request.form["student_count"],
        "student_array": request.form["student_array"],
        "exit_time": request.form["exit-time"],
        "guardian_name": request.form["name-guardian"],
        "guardian_relation": request.form["guardian-relation"],
        "guardian_email": request.form["email"],
        "reason_for_gatepass": request.form["about"]
    }
    studentdataArray = form_data["student_array"].split(",")
    perStudentSublist = [studentdataArray[x:x+3] for x in range(0, len(studentdataArray), 3)]
    number_of_students = len(studentdataArray)
    #print(list_count)
    # Working implementation, but slower by design- sends x queries depending on the no. of children
    """ for i in perStudentSublist:
        query = f"CALL insert_data('{i[0]}', '{i[1]}', '{i[2]}', {int(form_data["student_type"])}, '{form_data["exit_time"]}', '{form_data["guardian_name"]}', '{form_data['guardian_relation']}', '{form_data['guardian_email']}', '{form_data['reason_for_gatepass']}');"
        try:
            print(query)
            #data.query_db(query, True)
            data.commandquery(query)
            #return redirect(current_app.config['FRONTEND_URL']+"/request-a-gatepass")
            #"http://localhost:5173")
        except:
            pass """
    # Faster implementation (hopefully)
    query = """INSERT INTO public.requests (student_name, student_email, student_grade, student_type_id, exit_time, guardian_name, guardian_relation, guardian_email, reason) VALUES"""
    for i in perStudentSublist:
        query += f"""('{i[0]}', '{i[1]}', '{i[2]}', {int(form_data["student_type"])}, '{form_data["exit_time"]}', '{form_data["guardian_name"]}', '{form_data['guardian_relation']}', '{form_data['guardian_email']}', '{form_data['reason_for_gatepass']}'),"""

    query = query[:-1]
    try:
            print(query)
            #data.query_db(query, True)
            data.commandquery(query)
            #return redirect(current_app.config['FRONTEND_URL']+"/request-a-gatepass")
            #"http://localhost:5173")
    except:
        pass

    return redirect(current_app.config['FRONTEND_URL'] +"/request-a-gatepass")



"""     if(list_count > 0):
        #counter =studentdataArray.count/3
        for i in range(0,list_count):
            studentdata_1 = studentdataArray[i:3]
            #studentdata = studentdata
            #print(studentdata_1)
            query = f"CALL insert_data('{studentdata_1[0]}', '{studentdata_1[1]}', '{studentdata_1[2]}', {int(form_data["student_type"])}, '{form_data["exit_time"]}', '{form_data["guardian_name"]}', '{form_data['guardian_relation']}', '{form_data['guardian_email']}', '{form_data['reason_for_gatepass']}');
            
 """    #query = f"""CALL insert_data('Yassss', 'studentEmail@example.com', '{form_data["grade"]}', {int(form_data["student_type"])}, '{form_data["exit_time"]}', '{form_data["guardian_name"]}', '{form_data['guardian_relation']}', '{form_data['guardian_email']}', '{form_data['reason_for_gatepass']}');"""
# update stored procedure for processing guardian details and email + reason

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
    userdata =json.loads(request.data)
    useremail= userdata["user_email"]
    query = f"""Select guardian_id, primary_guardian_email ,secondary_guardian_email,primary_contactnumber,seconday_contactnumber, student_list from guardian Where created_by='{useremail}' order by created_on  desc Limit 1;"""
   
    dbdata =data.getdata_Json(query)

    response = json.loads(json.dumps(dbdata))
    return send_request(response)
    
def send_request(data):
    request = jsonify(data)
    request.headers.add("Access-Control-Allow-Origin", "*")
    return request

@bp.route("/userrequests", methods = ["POST"])
def get_user_requests():
    userdata =json.loads(request.data)
    useremail= userdata["user_email"]
    print("flask==" +useremail)
    query=f"""SELECT * FROM get_userrequests('{useremail}')"""
    print(query)
    return send_request(data.query_db(query))