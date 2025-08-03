from flask_sqlalchemy import SQLAlchemy
from flask import Flask

# Initialize SQLAlchemy
db = SQLAlchemy()

def init_db(app):
    # Configure PostgreSQL connection
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:12345678@localhost:5432/embedded'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize DB with app
    db.init_app(app)
