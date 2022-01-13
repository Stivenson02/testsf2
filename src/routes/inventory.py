from flask import Blueprint, render_template

inventory = Blueprint('inventory', __name__)

@inventory.route('/inventory_show')
def inventory_show():
    return render_template('inventory.html')

@inventory.route('/add_inventory')
def add_inventory():
    return 'add_inventory'

@inventory.route('/edit_inventory')
def edit_inventory():
    return 'edit_inventory'

@inventory.route('/delete_inventory')
def delete_inventory():
    return 'delete_inventory'

@inventory.route('/get_inventory')
def get_inventory():
    return 'get_inventory'