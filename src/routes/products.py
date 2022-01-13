from flask import Blueprint, render_template

products = Blueprint('products', __name__)

@products.route('/products_show')
def products_show():
    return render_template('products.html')

@products.route('/add_products')
def add_products():
    return 'add_products'

@products.route('/edit_products')
def edit_products():
    return 'edit_products'

@products.route('/delete_products')
def delete_products():
    return 'delete_products'

@products.route('/get_products')
def get_products():
    return 'get_products'