# -*- coding: utf-8 -*-

from bikeparking import *
from bikeparking.bikeparking_blueprint import bikeparking
from bikeparking.database import dao
from bikeparking.model.parking import Parking

@bikeparking.route('/test')
def test():
    bikeparking_data = dao
    return render_template('test.html', bikeparking=bikeparking_data)