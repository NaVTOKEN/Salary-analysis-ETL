from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from scripts.etl import run_etl

with DAG(
    "salary_etl_pipeline",
    start_date=datetime(2024, 1, 1),
    schedule_interval="@daily",
    catchup=False
) as dag:

    etl_task = PythonOperator(
        task_id="run_etl",
        python_callable=run_etl
    )
