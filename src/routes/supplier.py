from flask import Blueprint, render_template

supplier = Blueprint('supplier', __name__)

@supplier.route('/supplier_show')
def supplier_show():
    return render_template('supplier.html')

@supplier.route('/add_supplier')
def add_supplier():
    return 'add_supplier'

@supplier.route('/edit_supplier')
def edit_supplier():
    return 'edit_supplier'

@supplier.route('/delete_supplier')
def delete_supplier():
    return 'delete_supplier'

@supplier.route('/get_supplier')
def get_supplier():
    return 'get_supplier'