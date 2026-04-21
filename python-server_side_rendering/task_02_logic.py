#!/usr/bin/python3
"""
Flask application demonstrating Jinja loops and conditions.
"""
from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/items')
def items():
    """Reads items from JSON file and renders them."""
    try:
        with open('items.json', 'r') as f:
            data = json.load(f)
            # JSON-dan "items" siyahısını götürürük
            items_list = data.get('items', [])
    except (FileNotFoundError, json.JSONDecodeError):
        items_list = []
        
    return render_template('items.html', items=items_list)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
