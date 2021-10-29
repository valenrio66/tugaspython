# -*- coding: utf-8 -*-
"""
Created on Fri Oct 29 15:19:26 2021

@author: Acer
"""

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"