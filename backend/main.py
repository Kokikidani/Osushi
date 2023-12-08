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

@app.route('/suggestion')
def suggestion():
    df = pd.read_csv('xxx.csv')

@app.route('/ranking')
def ranking():
    return render_template(
        'ranking.html'
    )
def count(): #CSVファイルのうち必要なものだけをピックアップして行き先の数をカウントする。
    csv_dirs = os.listdir('/Users/ryoyajindo/daijikken/data_result')
    for csv_dir in csv_dirs:
        folder_path = '/Users/ryoyajindo/daijikken/data_result/' + csv_dir
        csv_files = os.listdir(folder_path) #csv_files[0]にある日のcsvファイルが入ってる。
        for csv_file in csv_files:
            df = pd.read_csv(csv_file)