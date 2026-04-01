# Salary-analysis-ETL
End to end salary analysis

Salary Intelligence ETL Pipeline

Overview

End-to-end Data Engineering project to process and analyze employee salary data across departments using Batch + Streaming pipelines.

---

 Tech Stack

- Python (Pandas, SQLAlchemy)
- PySpark
- Apache Kafka
- PostgreSQL
- Apache Airflow
- Docker

---

 Architecture

CSV/API → Kafka → Spark → PostgreSQL → SQL Analytics → Airflow

---

Pipeline

- Extract: CSV + Kafka streaming
- Transform: Cleaning, standardization, salary categorization
- Load: PostgreSQL (staging → cleaned → analytics)
- Orchestrate: Airflow DAG

---

Key Analytics

- Avg salary per department
- Top earners (window functions)
- Salary distribution
- Anomaly detection

---

 Structure

salary-intelligence-platform/
├── data/
├── kafka/
├── spark/
├── scripts/
├── airflow/
├── sql/
├── docker/
├── README.md

---

 Run

docker-compose up
python scripts/etl.py
python kafka/producer.py
spark-submit spark/transformation.py

---

 Highlights

- Batch + Streaming pipeline
- Incremental & scalable design
- Data validation checks
- Production-style architecture

---



