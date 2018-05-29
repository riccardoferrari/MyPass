from flask import Flask, render_template
from sqlite3 import connect

app = Flask(__name__, static_url_path='/static')

from .routes import *