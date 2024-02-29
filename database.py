import pymysql

# Connect to the database using PyMySQL
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