from flask import Flask, render_template
from routes.supplier import supplier
from routes.products import products
from routes.inventory import inventory
from flaskext.mysql import MySQL

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

# Router supplier
app.register_blueprint(supplier)


# Router products
app.register_blueprint(products)

# Router inventory
app.register_blueprint(inventory)

