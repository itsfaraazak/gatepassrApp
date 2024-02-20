import connect as db

def get_request():
    config = db.load_config()
    conn = db.connect(config)
    cursor = conn.cursor()
    cursor.execute("SELECT student_type_id, student_type FROM student_type;")
    return cursor.fetchall()

get_request()