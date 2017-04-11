# -*- coding: utf-8 -*-
from flask import render_template

from spidermanager import app


@app.route("/main", methods=['GET'])
def main():

    return render_template('main.html')