# -*- coding: utf-8 -*-
from flask import render_template, session, redirect, url_for

from spidermanager import app


@app.route("/main", methods=['GET'])
def main():
    if session.has_key('admin'):
        return render_template('main.html',admin=session['admin'])
    else:
        return redirect(url_for('login'))
