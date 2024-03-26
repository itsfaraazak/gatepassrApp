from . import connect as db
#import connect as db
"""
query_requests = "SELECT req.student_name, req.student_email, student_grade, req.student_type_id, exit_time
,st_type.student_type,approved_by
FROM requests req
join public.student_type st_type
on req.student_type_id = st_type.student_type_id
"


def get_request():
    cursor, conn = get_db_connection()
    cursor.execute("SELECT student_type_id, student_type FROM student_type;")
    data = cursor.fetchall()
    disconnect(cursor, conn)
    return data

"""

#def get_db_connection():
#    config = db.load_config()
#    conn = db.connect(config)
#    cursor = conn.cursor()
#    return cursor, conn

def query_db(query, is_stored_procedure = False):
    cursor, conn = db.connect()
    cursor.execute(query)
    if is_stored_procedure == False:
        print("2")
        data = cursor.fetchall()
        disconnect(cursor, conn)
        return data
    else:
        print("1")
        data = cursor.fetchone()
        print(data)
        disconnect(cursor, conn)
        return data
    #else: pass
    disconnect(cursor, conn)

def commandquery(query):
    print("command query")
    cursor, conn = db.connect()
    cursor.execute(query)
    disconnect(cursor, conn)
    return ""

"""
def insert_request_data(data):
    cursor, conn = get_db_connection()
    exit_time = data['exit_time']
    grade = data['grade']
    #exit_time = unformat_exit_time.replace("T", " ")
    query = f"CALL insert_data('John Doe Student', 'studentEmail@example.com', '{grade}', 3, '{exit_time}');"
    print(query)
    cursor.execute(query)
    disconnect(cursor, conn)
    return ""

"""

def disconnect(cursor, conn):
    conn.commit()
    cursor.close()
    conn.close()

from psycopg2.extras import RealDictCursor

def getdata_Json(query):
    cursor, conn = db.connect()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    query_sql = query
    cur.execute(query_sql)
    results = cur.fetchall()
    disconnect(cursor, conn)
    return results
# get_request()