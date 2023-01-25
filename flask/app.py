from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import UniqueConstraint

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.sql"
CORS(app)

db = SQLAlchemy(app)
migrate = Migrate(app, db)


class Product(db.Model):
    """Product Class"""
    id = db.Column(db.Integer, primary_key=True, autoincrement=False)
    title = db.Column(db.String(200))
    image = db.Column(db.String(200))


class ProductUser(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    product_id = db.Column(db.Integer)

    UniqueConstraint("user_id", "product_id", name="user_product_unique")


@app.route("/")
def home():
    return "Hello"


if __name__ == "__main__":
    app.run(debug=True, port=5001)
