from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')

def home():
    return render_template('home.html')

@app.route('/supplier')

def supplier():
    return render_template('supplier.html')

@app.route('/products')

def products():
    return render_template('products.html')

@app.route('/inventory')

def inventory():
    return render_template('inventory.html')

if __name__ == '__main__':
    app.run(debug=True)