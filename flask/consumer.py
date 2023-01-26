import json

import pika

from app import Product, db, app

params = pika.URLParameters(
    "amqps://yyixeqjd:ShEneQHotFeYrXpwh0ilhq9AaChezU8g@kangaroo.rmq.cloudamqp.com/yyixeqjd"
)
connection = pika.BlockingConnection(params)
channel = connection.channel()

channel.queue_declare(queue="flask")


def callback(ch, method, properties, body):
    with app.app_context():
        print("received from main app!")
        property = properties.content_type
        body = json.loads(body)
        print(body)

        id_ = body.get("id")
        title = body.get("title")
        image = body.get("image")

        if property == "product created":
            product = Product(id=id_, title=title, image=image)
            db.session.add(product)
            db.session.commit()

        elif property == "product updated":
            product = Product.query.get(id_)
            product.title = title
            product.image = image
            db.session.commit()

        elif property == "product deleted":
            product = Product.query.get(id_)
            db.session.delete(product)
            db.session.commit()


channel.basic_consume(queue="flask", on_message_callback=callback, auto_ack=True)
print("Consuming started on flask")
channel.start_consuming()
channel.close()
