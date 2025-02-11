# Kafka Producer for Real-Time Stock Data Streaming

## Overview
This project sets up a **Kafka Producer** to stream real-time stock market data. It reads stock data from a CSV file and continuously sends random records to a Kafka topic. This implementation is useful for **real-time data processing, analytics, and machine learning pipelines**.

## Prerequisites
- Python 3.x
- Apache Kafka setup
- A CSV dataset containing stock market data

## Installation
Ensure you have Kafka and Python installed. Then, install the required Kafka Python library:
```bash
pip install kafka-python pandas
```

## Implementation Details
### 1. Initialize Kafka Producer
The script initializes a Kafka producer that connects to a Kafka broker (modify the IP accordingly):
```python
from kafka import KafkaProducer
from json import dumps

producer = KafkaProducer(
    bootstrap_servers=[':9092'],  # Update with actual Kafka broker IP
    value_serializer=lambda x: dumps(x).encode('utf-8')
)
```

### 2. Load Stock Market Data
The script reads a CSV file (`indexProcessed.csv`) containing stock market data:
```python
import pandas as pd

df = pd.read_csv("data/indexProcessed.csv")
print(df.head())
```

### 3. Send Data to Kafka Topic
The script continuously selects a random stock entry from the dataset and sends it to the Kafka topic **'demo_test'**:
```python
from time import sleep

while True:
    dict_stock = df.sample(1).to_dict(orient="records")[0]
    producer.send('demo_test', value=dict_stock)
    sleep(1)
```

### 4. Flush Kafka Messages
Ensures that any unsent messages are pushed to the Kafka topic before termination:
```python
producer.flush()
```

## Usage
Run the script to start streaming stock data:
```bash
python kafka_producer.py
```

## Live Dashboard with Amazon QuickSight
Later, we use **Amazon QuickSight** to create a **live dashboard** that visualizes real-time stock market data. The streamed data from Kafka is stored in **Amazon S3**, queried via **Amazon Athena**, and dynamically visualized in **QuickSight** for actionable insights.

## Notes
- Update the `bootstrap_servers` with your Kafka broker IP.
- Ensure Kafka is running before executing the script.
- Modify the `sleep(1)` interval for different message frequency.

## License
This project is open-source and available for educational purposes.

