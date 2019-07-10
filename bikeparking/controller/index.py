# -*- coding: utf-8 -*-

from flask import render_template

from bikeparking.bikeparking_blueprint import bikeparking

@bikeparking.route('/')
def index():
    return render_template('index.html')