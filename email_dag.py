from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
from email_check import check_email  # Import your email check function
from slack_alert import send_slack_alert  # Import your Slack alert function

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 12, 15),  # Date when you want your DAGs to ge started
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'check_email_dag',
    default_args=default_args,
    description='A simple email check DAG for Completed folder',
    schedule_interval='30 * * * *',  # Run at 30th minute every hour. You can change accordingly
)

def check_and_alert():
    if not check_email():  # If emails are not found
        send_slack_alert()  # Send out a slack alert

check_email_task = PythonOperator(
    task_id='check_email_task',
    python_callable=check_and_alert,
    dag=dag,
)

check_email_task
