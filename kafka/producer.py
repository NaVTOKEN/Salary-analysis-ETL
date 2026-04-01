from kafka import KafkaProducer
import json
import time
import random

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

departments = ["IT", "HR", "FINANCE"]

while True:
    data = {
        "emp_id": random.randint(100, 999),
        "department": random.choice(departments),
        "salary": random.randint(30000, 150000)
    }

    producer.send("salary_topic", data)
    print(f"Sent: {data}")
    time.sleep(2)
