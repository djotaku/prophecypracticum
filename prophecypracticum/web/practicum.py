"""The main logic for the web page."""

from flask import Blueprint, session, flash, g, redirect, render_template, request, url_for
from werkzeug.exceptions import abort

from prophecypracticum.web.auth import login_required
from prophecypracticum.engine.prophecy import Prophecy

bp = Blueprint('practicum', __name__)


@bp.route('/')
@login_required
def index():
    return render_template('practicum/index.html')


@bp.route('/prophecy/create', methods=('GET', 'POST'))
@login_required
def create_prophecy():
    if request.method == 'POST':
        prophecy = request.form['prophecy']
        current_prophecy = Prophecy()
        # need to get the supplicant from the database and need to have it be a field below.
        current_prophecy.modify_text_prophecy(session['user_id'], prophecy)
        return redirect(url_for('practicum.index'))

    return render_template('practicum/create_prophecy.html')

# for listing prophecies, use something similar to the blog template (from flask example) with the Jinja loop.
