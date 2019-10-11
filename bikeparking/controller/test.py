# -*- coding: utf-8 -*-

import pymysql

from flask import render_template, current_app
from bikeparking.bikeparking_blueprint import bikeparking

@bikeparking.route('/test')
def test():
    db_address = current_app.config['DB_ADDRESS']
    db_port = current_app.config['DB_PORT']
    db_id = current_app.config['DB_ID']
    db_password = current_app.config['DB_PASSWORD']
    db_name = current_app.config['DB_NAME']

    conn = pymysql.connect(host=db_address,
                          port=int(db_port),
                          user=db_id,
                          password=db_password,
                          db=db_name,
                          charset='utf8')

    try:
        cursor = conn.cursor()
        sql = "SELECT * FROM parking"
        cursor.execute(sql)
        rows = cursor.fetchall()

        for row_data in rows:
            print(row_data[0])
            print(row_data[1])
            print(row_data[2])
            print(row_data[3])
            print(row_data[4])
            print(row_data[5])
    finally:
        conn.close()


    return render_template('test.html')