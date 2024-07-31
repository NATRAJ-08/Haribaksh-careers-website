import pymysql
import os

my_secret = os.environ['PASSWORD']


def load_jobs_from_db():
    connection = pymysql.connect(
        charset="utf8mb4",
        connect_timeout=10,
        cursorclass=pymysql.cursors.DictCursor,
        db="defaultdb",
        host="haribakshcareers-natraj-careers.a.aivencloud.com",
        password=my_secret,
        read_timeout=10,
        port=28698,
        user="avnadmin",
        write_timeout=10,
    )

    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM jobs")
        job = cursor.fetchall()
        jobs = [dict(row) for row in job]

    connection.close()

    return jobs


def load_job_from_db(id):
    connection = pymysql.connect(
        charset="utf8mb4",
        connect_timeout=10,
        cursorclass=pymysql.cursors.DictCursor,
        db="defaultdb",
        host="haribakshcareers-natraj-careers.a.aivencloud.com",
        password=my_secret,
        read_timeout=10,
        port=28698,
        user="avnadmin",
        write_timeout=10,
    )

    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM jobs WHERE id = %s", (id, ))
        job = cursor.fetchone()

    connection.close()

    if job:
        return dict(job)
    else:
        return None


def add_application_to_db(job_id, data):
    connection = pymysql.connect(
        charset="utf8mb4",
        connect_timeout=10,
        cursorclass=pymysql.cursors.DictCursor,
        db="defaultdb",
        host="haribakshcareers-natraj-careers.a.aivencloud.com",
        password=my_secret,
        read_timeout=10,
        port=28698,
        user="avnadmin",
        write_timeout=10,
    )

    with connection.cursor() as cursor:
        query = "INSERT INTO applications (job_id, full_name, email, linkedin_url, education, work_experience, resume_url) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        cursor.execute(
            query,
            (job_id, data['full_name'], data['email'], data['linkedin_url'],
             data['education'], data['work_experience'], data['resume_url']))

    connection.commit()
    connection.close()


def get_user_by_username(username):
    connection = pymysql.connect(
        charset="utf8mb4",
        connect_timeout=10,
        cursorclass=pymysql.cursors.DictCursor,
        db="defaultdb",
        host="haribakshcareers-natraj-careers.a.aivencloud.com",
        password=my_secret,
        read_timeout=10,
        port=28698,
        user="avnadmin",
        write_timeout=10,
    )

    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM users WHERE username = %s", (username, ))
        user = cursor.fetchone()

    connection.close()

    if user:
        return dict(user)
    else:
        return None


def add_user_to_db(username, password_hash):
    connection = pymysql.connect(
        charset="utf8mb4",
        connect_timeout=10,
        cursorclass=pymysql.cursors.DictCursor,
        db="defaultdb",
        host="haribakshcareers-natraj-careers.a.aivencloud.com",
        password=my_secret,
        read_timeout=10,
        port=28698,
        user="avnadmin",
        write_timeout=10,
    )

    with connection.cursor() as cursor:
        query = "INSERT INTO users (username, password_hash) VALUES (%s, %s)"
        cursor.execute(query, (username, password_hash))

    connection.commit()
    connection.close()
