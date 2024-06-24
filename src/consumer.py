#!/usr/bin/env python3
import pika, sys, os, json

from utils.apify import add_new_ig_username_to_actor

def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='new_ig_username')

    def callback(ch, method, properties, body):
        body = json.loads(body)
        print(" [x] Received %r" % body)
        add_new_ig_username_to_actor(body["new_username"])

    channel.basic_consume(queue='new_ig_username', on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)#!/usr/bin/env python3