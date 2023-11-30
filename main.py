from Osushi import app
from flask import render_template
#import pandas as pd

@app.route('/')
def index():
    print("render index.html")
    return render_template(
        'index.html'
    )

@app.route('/form')
def form():
    return render_template(
        'form.html'
    )