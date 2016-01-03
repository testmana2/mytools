__author__ = 'thomas'

from flask import session, redirect, url_for, render_template_string, request
from . import subapp

@subapp.route('/', methods=['GET', 'POST'])
def index():
    return 'Hello! ss!'
