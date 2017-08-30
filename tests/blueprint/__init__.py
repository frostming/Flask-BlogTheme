from flask import Blueprint, render_template_string


sub = Blueprint('sub', __name__)


@sub.route('/')
def index():
    return render_template_string('{{blueprint}}')
