import connect as db

query_requests = """SELECT req.student_name, req.student_email, student_grade, req.student_type_id, exit_time
,st_type.student_type,approved_by
FROM requests req
join public.student_type st_type
on req.student_type_id = st_type.student_type_id
"""

def get_request():
    cursor, conn = get_db_connection()
    cursor.execute("SELECT student_type_id, student_type FROM student_type;")
    data = cursor.fetchall()
    disconnect(cursor, conn)
    return data

def get_db_connection():
    config = db.load_config()
    conn = db.connect(config)
    cursor = conn.cursor()
    return cursor, conn

def get_data(query):
    cursor, conn = get_db_connection()
    cursor.execute(query)
    data = cursor.fetchall()
    disconnect(cursor, conn)
    return data

def insert_request_data(data):
    cursor, conn = get_db_connection()
    exit_time = data['exit_time']
    #exit_time = unformat_exit_time.replace("T", " ")
    query = f"""CALL insert_data('John Doe Student', 'studentEmail@example.com', '20', 3, '{exit_time}');"""
    print(query)
    cursor.execute(query)
    disconnect(cursor, conn)
    return ""

def disconnect(cursor, conn):
    conn.commit()
    cursor.close()
    conn.close()



get_request()