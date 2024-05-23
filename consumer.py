#!/usr/bin/env python
import pika, sys, os, time, json
from logic import count_people_on_img_from_url

def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost', 5672))
    channel = connection.channel()
    channel.queue_declare(queue='img_processing')
    channel.basic_qos(prefetch_count=1)

    def callback(ch, method, properties, body):
        message = json.loads(body)
        for img_id, url in message.items():
            count_people_on_img_from_url(url,img_id)
        ch.basic_ack(delivery_tag = method.delivery_tag)

    channel.basic_consume(queue='img_processing', auto_ack=False, on_message_callback=callback)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

    connection.close()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)

