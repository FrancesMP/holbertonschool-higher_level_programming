from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route('/items')
def items():
    try:
        with open('items.json', 'r') as f:
            data = json.load(f)
            items = data.get("items", [])
    except Exception:
        items = []
    return render_template('items.html', items=items)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
