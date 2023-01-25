import pika

params = pika.URLParameters(
    "amqps://yyixeqjd:ShEneQHotFeYrXpwh0ilhq9AaChezU8g@kangaroo.rmq.cloudamqp.com/yyixeqjd"
)
connection = pika.BlockingConnection(params)
channel = connection.channel()

channel.queue_declare(queue="admin")


def callback(ch, method, properties, body):
    print("received")
    print(body)


channel.basic_consume(queue="admin", on_message_callback=callback, auto_ack=True)
print("Consuming started")
channel.start_consuming()
channel.close()
