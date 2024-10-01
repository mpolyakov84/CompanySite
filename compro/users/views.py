from flask import render_template, url_for, redirect, flash, Blueprint, request
from flask_login import current_user, login_required, login_user, logout_user
from compro import db, login_manager
from compro.models import Users
from compro.users.forms import LoginForm, RegisterForm, PhotoForm

users_bp = Blueprint('users', __name__, template_folder='templates')

@users_bp.route('/register', methods=["GET", "POST"])
def register():

    form = RegisterForm()
    if form.validate_on_submit():

        user = Users(form.username.data, form.email.data, form.password.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('users.login'))

    return render_template('register.html', form=form)

@users_bp.route('/login', methods=["GET", "POST"])
def login():
    form = LoginForm()

    if form.validate_on_submit():

        user = Users.query.filter_by(email=form.email.data).first()
        if user != None and user.check_pass(form.password.data):

            login_user(user)
            flash(f'You are now logged in as {user.username}')

            next = request.args.get('next', url_for('core.index'))
            return redirect(next)

    return render_template('login.html', form=form)

@users_bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('core.index'))


@users_bp.route('/update', methods=["GET", "POST"])
@login_required
def update():

    form = RegisterForm()
    if form.validate_on_submit():


        db.session.commit()
        return redirect(url_for('users.login'))

    pic_form  = PhotoForm()
    if pic_form.validate_on_submit():
        pass
    return render_template('profile.html', form=form)


