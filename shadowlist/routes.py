__author__ = 'thomas'

from flask import current_app, session, redirect, url_for, render_template_string, request
from . import subapp
import json


@subapp.route('/', methods=['GET', 'POST'])
def index():
    items_file = current_app.config.get('SHADOW_ITEM_PATH', None)
    try:
        with open(items_file) as fp:
            item_list = json.load(fp)
            return '\n'.join([json.dumps(e) for e in item_list])
    except:
        return "load item list error!"

    return ''
