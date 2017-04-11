# -*- coding: utf-8 -*-
from spidermanager import app

from spidermanager.controller import main, user


if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000,debug=True)


def main():
    app.run(host='0.0.0.0',port=5000,debug=False)