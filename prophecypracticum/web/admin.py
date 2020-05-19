"""The main logic for the web page."""

from flask import Blueprint, flash, g, redirect, render_template, request, url_for
from werkzeug.exceptions import abort

from prophecypracticum.web.auth import login_required

from prophecypracticum.engine.controller import Controller

bp = Blueprint('admin', __name__)


@bp.route('/admin', methods=('GET', 'POST'))
@login_required
def admin():
    if request.method == 'POST':
        prophet = int(request.form['prophet'])
        supplicant = int(request.form['supplicant'])
        Controller.add_supplicant(prophet, supplicant)
        return redirect(url_for('admin.admin'))

    return render_template('practicum/admin.html')
