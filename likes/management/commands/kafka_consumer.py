from typing import Any
from django.core.management.base import BaseCommand
from confluent_kafka import Consumer
from collections import defaultdict
from django.db import transaction
from likes.models import *
import json
import os



class Command(BaseCommand):
    help = "Run Kafka consumer"

    def process_batch(self, like_batch):
        with transaction.atomic():
            for post_id, like_count in like_batch.items():
                post = Post.objects.get(id = post_id)
                post.like += like_count
                post.save()
        print(like_batch)

    def handle(self, *args: Any, **options):
        print("** Kafka Consumer started**")
        like_batch = defaultdict(int)
        conf = {
                'bootstrap.servers' : 'localhost:9092',
                'group.id' : 'location_group',
                'auto.offset.reset': 'earliest'
                }
        consumer = Consumer(conf)
        consumer.subscribe(['like_topic'])
        total_messages = 0 
        try:
            while True:
                print("** Listing for messages**")
                msg = consumer.poll(timeout = 1.0)
                if msg is None:
                    continue

                if msg.error():
                    print(msg.error())
                    continue

                data = json.loads(msg.value().decode('utf-8'))
                post_id = data['post_id']
                like_batch[post_id] += 1
                total_messages += 1
                print(f"like_batch - {like_batch}, total_messages - {total_messages}")
                if total_messages >= 10:
                    self.process_batch(like_batch)
                    like_batch.clear()
                    total_messages = 0

        except KeyboardInterrupt:
            pass
        finally:
            consumer.close()

