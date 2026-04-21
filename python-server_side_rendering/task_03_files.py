#!/usr/bin/python3
"""
Flask app to display products from JSON or CSV files.
"""
from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)

def read_json():
    with open('products.json', 'r') as f:
        return json.load(f)

def read_csv():
    products = []
    with open('products.csv', 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            row['id'] = int(row['id'])
            row['price'] = float(row['price'])
            products.append(row)
    return products

@app.route('/products')
def display_products():
    source = request.args.get('source')
    product_id = request.args.get('id', type=int)
    
    # 1. Mənbəni yoxla
    if source not in ['json', 'csv']:
        return render_template('product_display.html', error="Wrong source")
    
    # 2. Faylı oxu
    try:
        if source == 'json':
            products = read_json()
        else:
            products = read_csv()
    except Exception:
        return render_template('product_display.html', error="File not found")

    # 3. İD-yə görə filtrlə (əgər varsa)
    if product_id:
        filtered = [p for p in products if p['id'] == product_id]
        if not filtered:
            return render_template('product_display.html', error="Product not found")
        products = filtered

    return render_template('product_display.html', products=products)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
