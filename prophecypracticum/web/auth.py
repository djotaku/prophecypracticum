"""Authentication blueprint"""

import functools

from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for
from werkzeug.security import check_password_hash, generate_password_hash

from prophecypracticum.engine import user

bp = Blueprint('auth', __name__, url_prefix='/auth')  # all auth pages will be /auth/something


@bp.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        error = None

        if not username:
            error = "Username is required."
        elif not password:
            error = "Password is required."
        elif not email:
            error = "Email address is required"
        elif user.User.find_by_name(username):
            error = f"User {username} is already registered."

        if error is None:
            this_user = user.User(username, generate_password_hash(password), email)
            this_user.save_to_db()
            return redirect(url_for('auth.login'))

        flash(error)

    return render_template('auth/register.html')


@bp.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        error = None
        this_user = user.User.find_by_name(username)

        if this_user is None:
            error = "Incorrect username or password."
        elif not check_password_hash(this_user.password, password):
            error = "Incorrect username or password."

        if error is None:
            session.clear()
            session['user_id'] = this_user.id  # makes a cookie
            return redirect(url_for('index'))

        flash(error)

    return render_template('auth/login.html')


@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        g.user = user.User.find_by_id(user_id)


@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))


# create a decorator to require authentication in other views
def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))

        return view(**kwargs)

    return wrapped_view
