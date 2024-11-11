"""
Gabriel Orbe
Last Updated: Nov. 10, 2024

This file creates random data to emulate an e-commerce website and loads it to a Kafka topic
"""

from kafka import KafkaProducer
import json
import time
import random

# serialize json messages (KafkaProducer expects message data to be in bytes format)
producer = KafkaProducer(bootstrap_servers='localhost:9092', value_serializer=lambda v: json.dumps(v).encode('utf-8'))

# example product types and actions by customers
productTypes = ["clothing", "shoes", "electronics", "food", "beverages", "candles", "skincare"]
actions = ["view", "addToCard", "buy"]

# set up script to run for 10 minutes
startTime = time.time()
duration = 600 # 600 sec = 10 min

# create an event every 10 seconds 
while time.time() - startTime < duration:
    event = {
        "userId": random.randint(1, 100),
        "productId": random.choice(productTypes),
        "action": random.choice(actions),
        "timestamp": time.time()
    }
    producer.send('ecommerce-events', event)
    time.sleep(10)
