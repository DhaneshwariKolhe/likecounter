from confluent_kafka import Producer
import json
import os



conf = {
                'bootstrap.servers' : 'localhost:9092',
                }

producer = Producer(conf)


def delivery_report(err, msg):
    if err is not None:
        print('Message delivery failed: {}'.format(err))
    else:
        print('Message delivered to {} [{}]'.format(msg.topic(), msg.partition()))



def send_like_event(post_id):
    producer.produce('like_topic', key = str(post_id), value = json.dumps({
        "post_id": post_id
    }), callback=delivery_report)
print("Send to KAFKA")
producer.flush()