# -*- coding: utf-8 -*-

from flask import render_template

from bikeparking.bikeparking_blueprint import bikeparking

@bikeparking.route('/map')
def map():
    return render_template('map.html')