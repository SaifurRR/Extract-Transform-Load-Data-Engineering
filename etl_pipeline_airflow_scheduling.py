from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
import requests
import pandas as pd
import sqlalchemy

# Default arguments
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Define the DAG
with DAG(
    'etl_pipeline',
    default_args=default_args,
    description='An ETL pipeline example',
    schedule_interval=timedelta(days=1),
    start_date=datetime(2025, 1, 1),
    catchup=False,
) as dag:

    # Function to extract data from an API
    def extract():
        url = 'https://jsonplaceholder.typicode.com/posts'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            # Save extracted data to a CSV file
            pd.DataFrame(data).to_csv('/tmp/extracted_data.csv', index=False)
        else:
            raise Exception(f"Failed to fetch data: {response.status_code}")

    # Function to transform data
    def transform():
        # Load extracted data
        df = pd.read_csv('/tmp/extracted_data.csv')
        # Example transformation: Add a column
        df['extracted_at'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        # Save transformed data
        df.to_csv('/tmp/transformed_data.csv', index=False)

    # Function to load data into a database
    def load():
        # Connect to a SQLite database (can be replaced with other DBs)
        engine = sqlalchemy.create_engine('sqlite:///example.db')
        # Load transformed data
        df = pd.read_csv('/tmp/transformed_data.csv')
        # Save data to the database
        df.to_sql('posts', engine, if_exists='replace', index=False)

    # Define tasks
    extract_task = PythonOperator(
        task_id='extract',
        python_callable=extract,
    )

    transform_task = PythonOperator(
        task_id='transform',
        python_callable=transform,
    )

    load_task = PythonOperator(
        task_id='load',
        python_callable=load,
    )

    # Set dependencies
    extract_task >> transform_task >> load_task
