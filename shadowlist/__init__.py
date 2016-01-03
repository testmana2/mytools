
from flask import Blueprint

__author__ = 'thomas'

subapp = Blueprint('shadowlist', __name__)

from . import routes
