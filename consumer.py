import pika


def callback(ch, method, properties, body):
    print(f'{body} was consumed' + "\n")


def main():
    connection = pika.BlockingConnection(
        pika.ConnectionParameters('localhost', 5672, '/', pika.PlainCredentials("user", "password")))
    channel = connection.channel()
    channel.basic_consume(queue="my_app", on_message_callback=callback, auto_ack=True)
    channel.start_consuming()


if __name__ == "__main__":
    main()
