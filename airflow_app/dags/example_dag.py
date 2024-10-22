from airflow import DAG
from airflow.operators.dummy import DummyOperator
from datetime import datetime

# Define a minimal DAG
default_args = {
    'start_date': datetime(2024, 1, 1),
}

with DAG('example_dag', default_args=default_args, schedule_interval='@daily') as dag:
    start_task = DummyOperator(task_id='start')
