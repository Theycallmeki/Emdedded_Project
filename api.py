from flask import request, redirect, url_for, render_template
from models import Item
from db import db

# Create
def create_item():
    if request.method == 'POST':
        name = request.form['name']
        quantity = request.form['quantity']
        price = request.form['price']
        new_item = Item(name=name, quantity=int(quantity), price=float(price))
        db.session.add(new_item)
        db.session.commit()
    return redirect(url_for('main.items'))

# Update (now uses items.html)
def update_item(item_id):
    item = Item.query.get_or_404(item_id)
    if request.method == 'POST':
        item.name = request.form['name']
        item.quantity = int(request.form['quantity'])
        item.price = float(request.form['price'])
        db.session.commit()
        return redirect(url_for('main.items'))
    all_items = Item.query.all()
    return render_template('items.html', items=all_items, item_to_edit=item)

# Delete
def delete_item(item_id):
    item = Item.query.get_or_404(item_id)
    db.session.delete(item)
    db.session.commit()
    return redirect(url_for('main.items'))
