#!/usr/bin/env python3

from flask import Flask, render_template
from flask_bootstrap import Bootstrap
import json

app = Flask(__name__)
Bootstrap(app)

@app.route('/tables')

def tables():
    table_file = json.load(open('transactions.json', 'r'))
    table = table_file['valueRanges'][0]['values']
    return render_template('tables.html', table=table)

if __name__=='__main__':
    app.run()