import json

import pika

params = pika.URLParameters("amqps://yyixeqjd:ShEneQHotFeYrXpwh0ilhq9AaChezU8g@kangaroo.rmq.cloudamqp.com/yyixeqjd")
connection = pika.BlockingConnection(params)
channel = connection.channel()


def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange="", routing_key="flask", body=json.dumps(body), properties=properties)
    # channel.basic_publish(exchange="", routing_key="admin", body=b"Hello sending message to Admin")
    # channel.basic_publish(exchange="", routing_key="flask", body=b"Message to flask!")
