#!/usr/bin/python3
from flask import Flask, render_template, request
import json
import csv
import sqlite3

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

def read_sql():
    products = []
    conn = sqlite3.connect('products.db')
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute('SELECT name, category, price FROM Products')
    rows = cursor.fetchall()
    for row in rows:
        products.append(dict(row))
    conn.close()
    return products

@app.route('/products')
def display_products():
    source = request.args.get('source')
    product_id = request.args.get('id', type=int)
    
    if source not in ['json', 'csv', 'sql']:
        return render_template('product_display.html', error="Wrong source")
    
    try:
        if source == 'json':
            products = read_json()
        elif source == 'csv':
            products = read_csv()
        elif source == 'sql':
            products = read_sql()
            
        if product_id:
            products = [p for p in products if p.get('id') == product_id]
            if not products:
                return render_template('product_display.html', error="Product not found")
                
        return render_template('product_display.html', products=products)
    except Exception:
        return render_template('product_display.html', error="Data source error")

if __name__ == '__main__':
    app.run(debug=True, port=5000)
