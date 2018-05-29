from flask import Flask, render_template, url_for, redirect, url_for
from . import app

@app.route("/")
def index():
    return render_template('index.html')