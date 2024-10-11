import os, pika, json

rabbitmq_host = os.getenv('RABBITMQ_HOST', 'localhost')
rabbitmq_port = os.getenv('RABBITMQ_PORT', 5672)
credentials = pika.PlainCredentials('adsesugh', 'adsesugh')

parameters = pika.ConnectionParameters(host=rabbitmq_host,
                                       port=rabbitmq_port,
                                       virtual_host='/',
                                       credentials=credentials)

connection = pika.BlockingConnection(parameters)
channel = connection.channel()


def publish(routing_key, method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key=routing_key, body=body, properties=properties)
