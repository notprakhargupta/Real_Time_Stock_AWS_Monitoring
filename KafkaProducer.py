import pandas as pd
from kafka import KafkaProducer
from time import sleep
from json import dumps
import json

# Install Kafka Python Library
# pip install kafka-python

# Initialize Kafka Producer
producer = KafkaProducer(
    bootstrap_servers=[':9092'],  # Change IP here
    value_serializer=lambda x: dumps(x).encode('utf-8')
)

# Send a test message
producer.send('demo_test', value={'surname': 'parmar'})

# Read the dataset
df = pd.read_csv("data/indexProcessed.csv")
print(df.head())  # Display first few records

# Continuously send random stock data to Kafka topic
while True:
    dict_stock = df.sample(1).to_dict(orient="records")[0]
    producer.send('demo_test', value=dict_stock)
    sleep(1)

# Clear data from Kafka server
producer.flush()
