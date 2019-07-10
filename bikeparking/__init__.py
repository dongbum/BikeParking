# -*- coding: utf-8 -*-

from flask import Flask, render_template, request, url_for

def print_settings(config):
    print('===================================================================')
    print('settings for bike geometry')
    print('===================================================================')
    for key, value in config:
        print('%s=%s' % (key, value))
    print('===================================================================')

def not_found(error):
    return render_template('404.html'), 404

def create_app(config_filepath='resource/config.cfg'):
    bikeparking_app = Flask(__name__)

    return bikeparking_app