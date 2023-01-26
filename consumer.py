import json
import os

import pika
import django
from django.conf import settings



# Added this because consumer is outsider django
settings.configure()
django.setup()
from core.models import Project

params = pika.URLParameters(
    "amqps://yyixeqjd:ShEneQHotFeYrXpwh0ilhq9AaChezU8g@kangaroo.rmq.cloudamqp.com/yyixeqjd"
)
connection = pika.BlockingConnection(params)
channel = connection.channel()

channel.queue_declare(queue="admin")


def callback(ch, method, properties, body):
    print("received on admin")
    id_ = json.loads(body)
    project = Project.objects.get(id=id)
    project.likes += 1
    project.save()
    print("Likes added")


channel.basic_consume(queue="admin", on_message_callback=callback, auto_ack=True)
print("Consuming started")
channel.start_consuming()
channel.close()
