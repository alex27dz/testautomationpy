# example of working with MySQL

import mysql.connector


def mySQLfunc():
    print('Connect to MySQL server')
    db = mysql.connector.connect(
        host='localhost',  # ip when it will be on cloud
        user='root',
        passwd='NV27vnmc',
        database='data_list_storage'
    )
    print(db)  # checking our connection to DB
    mycursor = db.cursor()
    sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
    val = ("John", "Highway 21")
    mycursor.execute(sql, val)
    db.commit()
