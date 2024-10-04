from flask import render_template, Blueprint, redirect, url_for, flash, request
from compro.models import Blogs
from compro.blog.forms import PostForm
from flask_login import login_required, current_user
from compro import db

blog_bp = Blueprint('blog', __name__, template_folder='templates')

@blog_bp.route('/post/create', methods = ['GET', 'POST'])
@login_required
def create_post():

    form = PostForm()

    if form.validate_on_submit():
        post = Blogs(form.title.data,
                     form.content.data,
                     current_user.id)
        db.session.add(post)
        db.session.commit()
        flash('Your post has been created!', 'success')
        return redirect(url_for('blog.read_post', post_id=post.id))

    return render_template('create_post.html', form=form)

@blog_bp.route('/post/<int:post_id>')
def read_post(post_id):
    blog_post = Blogs.query.get_or_404(post_id)
    return render_template('blogpost.html', blog_post=blog_post)

@blog_bp.route('/post/update/<post_id>', methods = ['GET', 'POST'])
@login_required
def update_post(post_id):
    post = Blogs.query.get_or_404(post_id)

    if post.author != current_user:
        abort(403)


    form = PostForm()
    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data
        db.session.commit()
        flash('Your post has been updated!', 'success')
        return redirect(url_for('blog.read_post', post_id=post.id))

    elif request.method == 'GET':
        form.title.data = post.title
        form.content.data = post.content

    return render_template('create_post.html', form=form)

@blog_bp.route('/post/delete/<post_id>')
@login_required
def delete_post(post_id):
    post = Blogs.query.get_or_404(post_id)

    if post.author != current_user:
        abort(403)

    db.session.delete(post)
    db.session.commit()
    flash('Your post has been deleted!', 'success')
    return redirect(url_for('users.user_posts', user_id=current_user.id))
