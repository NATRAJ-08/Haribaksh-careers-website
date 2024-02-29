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
  