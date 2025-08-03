from flask import Blueprint, render_template, request
from models import Item
from api import create_item, update_item, delete_item

bp = Blueprint('main', __name__)

@bp.route('/')
def homepage():
    return render_template('homepage.html')

@bp.route('/items', methods=['GET', 'POST'])
def items():
    if request.method == 'POST':
        return create_item()
    items = Item.query.all()
    return render_template('items.html', items=items)

@bp.route('/items/<int:item_id>/edit', methods=['GET', 'POST'])
def edit_item(item_id):
    return update_item(item_id)

@bp.route('/items/<int:item_id>/delete', methods=['POST'])
def remove_item(item_id):
    return delete_item(item_id)

@bp.route('/inventory')
def inventory():
    items = Item.query.all()
    return render_template('inventory.html', items=items)

@bp.route('/pos')
def pos():
    return render_template('pos.html')
