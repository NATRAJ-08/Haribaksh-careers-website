import pymysql

# Connect to the database using PyMySQL
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
    result_pymysql = cursor.fetchall()

    print(result_pymysql)  
    for row in result_pymysql:
        print(dict(row))
connection.close()