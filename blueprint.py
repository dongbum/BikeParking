# -*- coding: utf-8 -*-

from flask import Blueprint

bikeparking = Blueprint('bikeparking', __name__, template_folder='../template', static_folder='../static')