import psycopg2

def connect(host="localhost", database="db_name", user="username", password="password"):
    """ Connect to the PostgreSQL database server """
    try:
        conn = psycopg2.connect(
            host=host, 
            database=database, 
            user=user, 
            password=password
        )
        return conn
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        raise

def getAllStudents():
    """ Retrieve all records from the students table """
    students = []
    try:
        with connect() as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM students")
                students = cur.fetchall()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        raise
    return students

def addStudent(first_name, last_name, email, enrollment_date):
    """ Insert a new student record """
    try:
        with connect() as conn:
            with conn.cursor() as cur:
                cur.execute(psycopg2.sql.SQL(f"INSERT INTO students ({first_name}, {last_name}, {email}, {enrollment_date}) VALUES"))
                conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        raise

def updateStudentEmail(student_id, new_email):
    """ Update email address for a student """
    try:
        with connect() as conn:
            with conn.cursor() as cur:
                cur.execute(psycopg2.sql.SQL(f"UPDATE students SET email = {new_email} WHERE student_id = {student_id}"))
                conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        raise

def deleteStudent(student_id):
    """ Delete a student record """
    try:
        with connect() as conn:
            with conn.cursor() as cur:
                cur.execute(psycopg2.sql.SQL(f"DELETE FROM students WHERE student_id = {student_id}"))
                conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        raise
