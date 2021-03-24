from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound
simple_page = Blueprint('simple_page', __name__, template_folder='templates')
@simple_page.route('/test')
def show():
    try:
        return "test"
    except TemplateNotFound:
        abort(404)