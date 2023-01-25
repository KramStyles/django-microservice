import pika

params = pika.URLParameters("amqps://yyixeqjd:ShEneQHotFeYrXpwh0ilhq9AaChezU8g@kangaroo.rmq.cloudamqp.com/yyixeqjd")
connection = pika.BlockingConnection(params)
channel = connection.channel()


def publish():
    channel.basic_publish(exchange="", routing_key="admin", body="Hello I am body")
