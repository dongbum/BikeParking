# -*- coding: utf-8 -*-

import os
from flask import Flask, render_template, request, url_for
from bikeparking.controller import *
from bikeparking.model import *

def print_settings(config):
    print('===================================================================')
    print('settings for bikeparking')
    print('===================================================================')
    for key, value in config:
        print('%s=%s' % (key, value))
    print('===================================================================')

def not_found(error):
    return render_template('404.html'), 404

def server_error(error):
    err_msg = str(error)
    return render_template('500.html', err_msg=err_msg), 500

def url_for_other_page(page):
    args = request.view_args.copy()
    args['page'] = page
    return url_for(request.endpoint, **args)

def create_app():
    bikeparking_app = Flask(__name__, instance_relative_config=True)

    print('instance_path:[%s]' % bikeparking_app.instance_path)

    from bikeparking.bikeparking_config import BikeParkingConfig
    bikeparking_app.config.from_object(BikeParkingConfig)
    bikeparking_app.config.from_pyfile('config.cfg', silent=True)
    print_settings(bikeparking_app.config.items())

    try:
        db_address = bikeparking_app.config['DB_ADDRESS']
        db_port = bikeparking_app.config['DB_PORT']
        db_id = bikeparking_app.config['DB_ID']
        db_password = bikeparking_app.config['DB_PASSWORD']
        db_name = bikeparking_app.config['DB_NAME']
    except ValueError:
        print("Cannot found DB connection info.")
        exit(1)

    # 로그 초기화
    from bikeparking.bikeparking_logger import Log
    log_filepath = os.path.join(bikeparking_app.instance_path, bikeparking_app.config['LOG_FILE_PATH'])
    Log.init(log_filepath=log_filepath)

    # 데이터베이스 처리

    from bikeparking.bikeparking_blueprint import bikeparking
    bikeparking_app.register_blueprint(bikeparking)

    bikeparking_app.error_handler_spec['404'] = not_found
    bikeparking_app.error_handler_spec['500'] = server_error

    bikeparking_app.jinja_env.globals['url_for_other_page'] = url_for_other_page

    return bikeparking_app