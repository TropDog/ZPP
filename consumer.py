#!/usr/bin/env python
import pika,time

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
channel.queue_declare(queue='hello')
channel.basic_qos(prefetch_count=1)

def callback(ch, method, properties, body):
    print(f" [x] Received {body}")
    time.sleep(1)
    ch.basic_ack(delivery_tag = method.delivery_tag)

channel.basic_consume(queue='hello', auto_ack=False, on_message_callback=callback)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()

connection.close()

