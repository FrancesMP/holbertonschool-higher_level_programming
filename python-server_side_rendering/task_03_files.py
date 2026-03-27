from flask import Flask, render_template, request
import json, csv

app = Flask(__name__)

def read_json():
    with open('products.json', 'r') as f:
        return json.load(f)

def read_csv():
    products = []
    with open('products.csv', newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            products.append({
                "id": int(row["id"]),
                "name": row["name"],
                "category": row["category"],
                "price": float(row["price"])
            })
    return products

@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id', type=int)
    data, error = [], None

    try:
        if source == 'json':
            data = read_json()
        elif source == 'csv':
            data = read_csv()
        else:
            error = "Wrong source"
    except Exception:
        error = "Error reading data."

    if not error and product_id:
        data = [p for p in data if p["id"] == product_id]
        if not data:
            error = "Product not found"

    return render_template("product_display.html", products=data, error=error)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
