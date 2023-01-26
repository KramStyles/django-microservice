from dataclasses import dataclass

from flask import Flask, jsonify, abort
from flask_cors import CORS
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
import requests
from sqlalchemy import UniqueConstraint

from producer import publish

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.sql"
CORS(app)

db = SQLAlchemy(app)
migrate = Migrate(app, db)


@dataclass
class Product(db.Model):
    """Product Class"""

    id: int
    title: str
    image: str

    id = db.Column(db.Integer, primary_key=True, autoincrement=False)
    title = db.Column(db.String(200))
    image = db.Column(db.String(200))


@dataclass
class ProductUser(db.Model):
    id: int
    user_id: int
    product_id: int

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    product_id = db.Column(db.Integer)

    UniqueConstraint("user_id", "product_id", name="user_product_unique")


@app.route("/")
def home():
    return "Hello"


@app.route("/api/products/")
def products():
    products = Product.query.all()
    return jsonify(products)


@app.route("/api/products/<int:id>/like/")
def like(id):
    response = requests.get("http://localhost:5000/api/users/random-user/")
    content = response.json()

    try:
        productUser = ProductUser(user_id=content["id"], product_id=id)
        db.session.add(productUser)
        db.session.commit()
        publish("product_liked", id)
    except Exception as err:
        abort(400, err)

    return jsonify({"message": "success"})


if __name__ == "__main__":
    app.run(debug=True, port=5001)
