import pika

params = pika.URLParameters(
    "amqps://yyixeqjd:ShEneQHotFeYrXpwh0ilhq9AaChezU8g@kangaroo.rmq.cloudamqp.com/yyixeqjd"
)
connection = pika.BlockingConnection(params)
channel = connection.channel()

channel.queue_declare(queue="main")


def callback(ch, method, properties, body):
    print("received from main app!")
    print(body)


channel.basic_consume(queue="admin", on_message_callback=callback)
print("Consuming started on flask")
channel.start_consuming()
channel.close()
