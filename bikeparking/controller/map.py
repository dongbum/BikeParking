# -*- coding: utf-8 -*-

import pymysql
from flask import render_template, current_app
from bikeparking.bikeparking_blueprint import bikeparking

@bikeparking.route('/map')
def map():
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
        sql = "SELECT  `no`,  LEFT(`name`, 256),  `longitude`,  `latitude`,  LEFT(`address`, 256),  LEFT(`operating_time`, 256),  LEFT(`operating_agency`, 256),  LEFT(`parking_count`, 256),  LEFT(`parking_type`, 256),  `charge`,  LEFT(`url`, 256),  LEFT(`phone`, 256),  `update_time` FROM `bikeparking`.`parking` LIMIT 1000;"
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

    return render_template('map.html', data=rows)