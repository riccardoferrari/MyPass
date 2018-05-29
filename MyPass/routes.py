from flask import Flask, render_template, url_for, redirect, url_for
from . import app
from .passwordGenerator import password


@app.route("/")
def index():
    return render_template('index.html')

@app.context_processor
def newPassword():
    return dict(mypass = password())