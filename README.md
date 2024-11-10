# E-commerce Pipeline
This is an ETL pipeline with random data to simulate e-commerce logs.

# Steps
Before running kafkaScript.py, make sure to do the following:
- $ pip install kafka-python
- Set up environment using Zookeeper (sample steps: https://kafka.apache.org/quickstart)
    - Start Zookeeper: $ bin/zookeeper-server-start.sh config/zookeeper.properties
    - Start Kafka: $ bin/kafka-server-start.sh config/server.properties
    - Create "ecommerce-events": $ bin/kafka-topics.sh --create --topic ecommerce-events --bootstrap-server localhost:9092

# Useful Links
Learning about Apache Kafka:
- https://kafka.apache.org/intro
- https://kafka.apache.org/quickstart

Kafka-Python library:
- https://kafka-python.readthedocs.io/en/master/#