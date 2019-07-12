# -*- coding: utf-8 -*-

from flask import render_template
from bikeparking.bikeparking_blueprint import bikeparking

@bikeparking.route('/test')
def test():
    return render_template('test.html')