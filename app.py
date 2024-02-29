from flask import Flask, render_template, jsonify
import pymysql

app = Flask(__name__)

def load_jobs_from_db():
    connection = pymysql.connect(
        charset="utf8mb4",
        connect_timeout=10,
        cursorclass=pymysql.cursors.DictCursor,
        db="defaultdb",
        host="haribakshcareers-natraj-careers.a.aivencloud.com",
        password="AVNS_1yapi6ol-2w_L7WvLpD",
        read_timeout=10,
        port=28698,
        user="avnadmin",
        write_timeout=10,
    )

    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM jobs")
        job = cursor.fetchall()

        # Convert the result to a list of dictionaries
        jobs = [dict(row) for row in job]

    connection.close()

    return jobs

@app.route('/')
def hello_world():
    jobs = load_jobs_from_db()
    return render_template('home.html',
                           jobs=jobs,
                           company_name='Haribaksh')

@app.route("/api/jobs")
def list_jobs():
    jobs = load_jobs_from_db()
    return jsonify(jobs)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=True)