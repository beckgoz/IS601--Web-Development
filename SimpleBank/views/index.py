from flask import Blueprint, render_template
home = Blueprint('home', __name__, url_prefix='/')
#bag27:4/29/2023    Created home landing page for bank
@home.route('/')
def index():
    return render_template("index.html")