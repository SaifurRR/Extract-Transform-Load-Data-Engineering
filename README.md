## ETL Airflow DAG Workflow:


from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator

# Define default arguments
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email': ['your_email@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Define the DAG
with DAG(
    'example_dag',
    default_args=default_args,
    description='A simple example DAG',
    schedule_interval=timedelta(days=1),
    start_date=datetime(2025, 1, 1),
    catchup=False,
) as dag:

    # Define Python functions
    def print_hello():
        print("Hello, Airflow!")

    def print_goodbye():
        print("Goodbye, Airflow!")

    # Define tasks
    task_1 = PythonOperator(
        task_id='say_hello',
        python_callable=print_hello,
    )

    task_2 = PythonOperator(
        task_id='say_goodbye',
        python_callable=print_goodbye,
    )

    # Set task dependencies
    task_1 >> task_2
