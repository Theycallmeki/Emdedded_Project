from flask import Flask
from db import init_db
from models import db
from urls import bp as routes

app = Flask(__name__)
init_db(app)

app.register_blueprint(routes)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
