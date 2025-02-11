from kafka import KafkaConsumer
from time import sleep
from json import dumps, loads
import json
from s3fs import S3FileSystem

# Initialize Kafka Consumer
consumer = KafkaConsumer(
    'demo_test',
    bootstrap_servers=[':9092'],  # Add your IP here
    value_deserializer=lambda x: loads(x.decode('utf-8'))
)

# Initialize S3 File System
s3 = S3FileSystem()

# Consume messages from Kafka and store them in S3
for count, i in enumerate(consumer):
    with s3.open(f"s3://kafka-stock-market-tutorial-youtube-darshil/stock_market_{count}.json", 'w') as file:
        json.dump(i.value, file)
