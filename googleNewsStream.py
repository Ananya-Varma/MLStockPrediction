from pygooglenews import GoogleNews
from utils import *
import pika


def main():
    gn = GoogleNews()
    fetched_queue = []
    filtered_queue = []
    invalid_url_queue = []
    query = "AAPL OR Apple"
    frequency = "1d"

    print("Fetching News From GoogleNews: ")

    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost', 5672, '/', pika.PlainCredentials('user', 'password')))
    channel = connection.channel()

    while True:

        news_object = gn.search(query=query, when=frequency)

        for news in news_object['entries']:
            story = get_story(news)
            if story not in fetched_queue:
                fetched_queue.append(story)

        print("Number of News Items fetched: " + str(len(fetched_queue)))

        for news in fetched_queue:
            if filter_url(news["link"]) and news not in filtered_queue:
                filtered_queue.append(news)

        print("Number of Items post filtering URL: " + str(len(filtered_queue)))

        for news in filtered_queue:
            status, content = get_article(news)
            news["content"] = content
            if status == False and news not in invalid_url_queue:
                invalid_url_queue.append(news)

        print("Number of Articles that couldn't get content: " + str(len(invalid_url_queue)))

        print("Sending News articles as Message Queues...")

        count = 0

        for news in filtered_queue:
            channel.basic_publish(exchange='my_exchange', routing_key='test', body=str(news))
            count = count + 1

        filtered_queue = []

        print("Number of messages sent in message queue: " + str(count))


if __name__ == "__main__":
    main()
