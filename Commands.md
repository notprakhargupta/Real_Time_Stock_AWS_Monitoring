Here’s your Kafka setup guide rewritten in a more structured and professional manner:  

---

# **Setting up Apache Kafka on AWS EC2**  
**By Prakhar Gupta**  

## **Step 1: Download and Extract Kafka**  
```bash
wget https://downloads.apache.org/kafka/3.3.1/kafka_2.12-3.3.1.tgz
tar -xvf kafka_2.12-3.3.1.tgz
```

## **Step 2: Install Java (If not installed)**  
Check Java version:  
```bash
java -version
```
If Java is not installed, install OpenJDK 1.8:  
```bash
sudo yum install java-1.8.0-openjdk
java -version
```
Navigate to the Kafka directory:  
```bash
cd kafka_2.12-3.3.1
```

## **Step 3: Start ZooKeeper**  
Kafka requires ZooKeeper to manage its distributed system. Start ZooKeeper with the following command:  
```bash
bin/zookeeper-server-start.sh config/zookeeper.properties
```

## **Step 4: Start Kafka Server**  
Open a new terminal session and SSH into your EC2 instance again. Then, execute the following commands:  
```bash
export KAFKA_HEAP_OPTS="-Xmx256M -Xms128M"
cd kafka_2.12-3.3.1
bin/kafka-server-start.sh config/server.properties
```

### **Configure Kafka to Run on a Public IP**  
Kafka is configured to run on a private server by default. To make it accessible via a public IP, modify the **server.properties** file:  
```bash
sudo nano config/server.properties
```
Find the line with `ADVERTISED_LISTENERS` and update it to use the public IP of your EC2 instance.

## **Step 5: Create a Kafka Topic**  
Open a new terminal session and execute:  
```bash
cd kafka_2.12-3.3.1
bin/kafka-topics.sh --create --topic demo_testing2 --bootstrap-server {Public_IP_of_EC2:9092} --replication-factor 1 --partitions 1
```

## **Step 6: Start Kafka Producer**  
Start a producer to send messages to the topic:  
```bash
bin/kafka-console-producer.sh --topic demo_testing2 --bootstrap-server {Public_IP_of_EC2:9092}
```
Once the producer starts, you can type messages and press **Enter** to send them.

## **Step 7: Start Kafka Consumer**  
Open a new terminal session and execute:  
```bash
cd kafka_2.12-3.3.1
bin/kafka-console-consumer.sh --topic demo_testing2 --bootstrap-server {Public_IP_of_EC2:9092}
```
This will start listening to the messages being produced.

---

Now, your Kafka setup is complete and you can start testing real-time data streaming between producers and consumers. 🚀
