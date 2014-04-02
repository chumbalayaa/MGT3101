from flask import render_template, url_for, redirect
from mgt3101 import app


@app.route('/'):
  return "It works!"
