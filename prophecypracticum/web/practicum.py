"""The main logic for the web page."""

from flask import Blueprint, flash, g, redirect, render_template, request, url_for
from werkzeug.exceptions import abort

from prophecypracticum.web.auth import login_required
from prophecypracticum.web.db import get_db

bp = Blueprint('practicum', __name__)


@bp.route('/')
@login_required
def index():
    return render_template('practicum/index.html')


@bp.route('/prophecy/create', methods=('GET', 'POST'))
@login_required
def create_prophecy():
    if request.method == 'POST':
        # this is where it will get the data to insert into prophecy database
        return redirect(url_for('practicum.index'))

    return render_template('practicum/create_prophecy.html')
