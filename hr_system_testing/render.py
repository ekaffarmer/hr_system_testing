# render.py
from crypt import methods
from statistics import median_grouped
from urllib import response
from flask import Flask
from flask import render_template, jsonify, request
from werkzeug.wrappers import Response
import config
import mysql.connector
from mysql.connector import Error
import json
# from jinja2.utils imsport msarkupsafe
# msarkupsafe.msarkup()
# msarkupsafe.msarkup('')
import datetime
import json

app = Flask(__name__)
app.config.from_object(config)

@app.route("/", methods = ['POST','GET'])
def index():
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="4rfv8uhb",
        database="hr"
    )
    db_Info = db.get_server_info()
    print("Database info: ", db_Info)

    cursor = db.cursor()
    
    if request.method == 'POST':
        print("The request method is 'POST'.")
        
        # get json passed from client side
        jsonData = request.get_json()
        # get comments if dict length > 1
        if (len(jsonData) > 1):
            comment0 = jsonData['0']['comment']['value']
            comment7 = jsonData['7']['comment']['value']
            print("Comment[0]: ", comment0)
            print("Comment[7]: ", comment7)
        # get cell values
        data = jsonData['data']
        print("data: ", data)
        # get staff
        staff = data[0][0]
        print("Shift of", staff, "is saved.")
        
        # # retrieve all start time
        # st_mon = data[1][1]
        # st_tue = data[1][2]
        # st_wed = data[1][3]
        # st_thu = data[1][4]
        # st_fri = data[1][5]
        # st_sat = data[1][6]
        # st_sun = data[1][7]

        # # retrieve all morning shift
        # ms_mon = data[2][1]
        # ms_tue = data[2][2]
        # ms_wed = data[2][3]
        # ms_thu = data[2][4]
        # ms_fri = data[2][5]
        # ms_sat = data[2][6]
        # ms_sun = data[2][7]

        # # retrieve all afternoon shift
        # as_mon = data[3][1]
        # as_tue = data[3][2]
        # as_wed = data[3][3]
        # as_thu = data[3][4]
        # as_fri = data[3][5]
        # as_sat = data[3][6]
        # as_sun = data[3][7]

        # # retrieve all evening shift
        # es_mon = data[4][1]
        # es_tue = data[4][2]
        # es_wed = data[4][3]
        # es_thu = data[4][4]
        # es_fri = data[4][5]
        # es_sat = data[4][6]
        # es_sun = data[4][7]

        # # retrieve all end time
        # et_mon = data[5][1]
        # et_tue = data[5][2]
        # et_wed = data[5][3]
        # et_thu = data[5][4]
        # et_fri = data[5][5]
        # et_sat = data[5][6]
        # et_sun = data[5][7]

        # staff_id is default to be 1
        # staff_id = 1

        # insert all shift
        # i = 0
        # while i < 5:
        #     sql = " INSERT INTO roster(staff_id, date, session_id, shift_id, update_by) VALUES(%s, %s, %s, %s, %s)"
        #     value = (staff_id, )
        
        
        return json.dumps(True)
    if request.method == 'GET':
        print("The request method is 'GET'.")
    else:
        print("Failed to save data.")

    cursor.close()
    db.close()
    return render_template("index.html")

@app.route("/save_name.html", methods = ['POST','GET'])
def save_name():
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="4rfv8uhb",
        database="hr"
    )

    db_Info = db.get_server_info()
    print("Database info: ", db_Info)

    cursor = db.cursor()

    if request.method == 'POST':
        fname = request.form['fname']
        lname = request.form['lname']
        print(fname)
        print(lname)
        sql = "INSERT INTO info(first_name, last_name) VALUES(%s, %s)"
        value = (fname, lname)

        cursor.execute(sql, value)
        db.commit()
    else:
        print("Failed to save data.")
    
    cursor.close()
    db.close()
    return render_template("save_name.html")
        
if __name__ == '__main__':
    app.run()