from flask import render_template, Blueprint
from compro.models import Users, Blogs

core_bp = Blueprint('core', __name__)

@core_bp.route('/')
def index():
    return render_template('index.html')