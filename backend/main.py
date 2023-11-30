from backend import app
from flask import render_template
import pandas as pd
import os

@app.route('/')
def index():
    return render_template(
        'index.html'
    )

@app.route('/form')
def form():
    return render_template(
        'form.html'
    )

@app.route('/ranking')
def ranking():
    return render_template(
        'ranking.html'
    )
def count(): #CSVファイルのうち必要なものだけをピックアップして行き先の数をカウントする。
    csv_file = os.listdir('/Users/ryoyajindo/daijikken/Osushi/backend/data_result')
    