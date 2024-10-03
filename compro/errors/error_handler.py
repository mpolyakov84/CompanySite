from flask import Blueprint, render_template

errors_bp = Blueprint('errors', __name__, template_folder='templates')

@errors_bp.app_errorhandler(404)
def error_404(error):
    return render_template('404.html', error=error), 404

@errors_bp.app_errorhandler(403)
def error_403(error):
    return render_template('403.html', error=error), 403
