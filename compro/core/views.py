from flask import render_template, Blueprint, request
from compro.models import Users, Blogs

core_bp = Blueprint('core', __name__)

@core_bp.route('/')
def index():
    page = request.args.get('page', 1, type=int)
    blog_posts = Blogs.query.order_by(Blogs.posted_date.desc()).paginate(page=page, per_page=3)
    return render_template('index.html', blog_posts=blog_posts, page=page)