# ***************************************************************************
#                       =========== datasprints ================
# Teste Técnico de Engenharia de Dados
# DAG - Copy from S3 - faz o download dos arquivos do s3 para o container.
# Candidato : Luiz Vinicius Izidorio Vidal
# ***************************************************************************

import os
from pathlib import Path

from airflow.models import Variable
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta
import requests
import sys

args = {
    'owner': 'luiz-vidal',
    'start_date': datetime(2020, 8, 1),
    'depends_on_past': False,
    'retries': 3,
    'retry_delay': timedelta(minutes=5),
    'email_on_retry': True,
    'email_on_failure': True,
}

job_info = {
    "extractJSON2009": {
        "bucketname": "https://s3.amazonaws.com/data-sprints-eng-test",
        "bashcommand": "curl -k -X GET",
        "remote_file": "data-sample_data-nyctaxi-trips-2009-json_corrigido.json",
        "local_file": f"{AIRFLOW_HOME}/data/json/nyc_2009.json"
    },
    "extractJSON2010": {
        "bucketname": "https://s3.amazonaws.com/data-sprints-eng-test",
        "bashcommand": "curl -k -X GET",
        "remote_file": "data-sample_data-nyctaxi-trips-2010-json_corrigido.json",
        "local_file": f"{AIRFLOW_HOME}/data/json/nyc_2010.json"
    },
    "extractJSON2011": {
        "bucketname": "https://s3.amazonaws.com/data-sprints-eng-test",
        "bashcommand": "curl -k -X GET",
        "remote_file": "data-sample_data-nyctaxi-trips-2011-json_corrigido.json",
        "local_file": f"{AIRFLOW_HOME}/data/json/nyc_2011.json"
    },
    "extractJSON2012": {
        "bucketname": "https://s3.amazonaws.com/data-sprints-eng-test",
        "bashcommand": "curl -k -X GET",
        "remote_file": "data-sample_data-nyctaxi-trips-2012-json_corrigido.json",
        "local_file": f"{AIRFLOW_HOME}/data/json/nyc_2012.json"
    },
    "extractCSVPayment": {
        "bucketname": "https://s3.amazonaws.com/data-sprints-eng-test",
        "bashcommand": "curl -k -X GET",
        "remote_file": "data-payment_lookup-csv.csv",
        "local_file": f"{AIRFLOW_HOME}/data/csv/nyc_payment.csv"
    },
    "extractCSVVendor": {
        "bucketname": "https://s3.amazonaws.com/data-sprints-eng-test",
        "bashcommand": "curl -k -X GET",
        "remote_file": "data-vendor_lookup-csv.csv",
        "local_file": f"{AIRFLOW_HOME}/data/csv/nyc_vendor.csv"
    }
}

# Airflow Variables
AIRFLOW_HOME = Path(os.environ.get("AIRFLOW_HOME", "~/airflow"))

for arquivo, val in job_info.items():

    dag_name = "copy_from_s3"

    bucketname = val['bucketname']
    bashcommand = val['bashcommand']
    remote_file = val['remote_file']
    local_file = val['local_file']

    dag = DAG(
        dag_id=dag_name,
        default_args=args,
        catchup=False,
        schedule_interval='30 3 * * *')  # 00:30 GMT-3

    with open(f'{AIRFLOW_HOME}/dags/copy/copy_s3.md', 'r') as f:
        dag.doc_md = f.read()

    start_log = DummyOperator(
        task_id='start_log',
        dag=dag)

    get_file = BashOperator(
        task_id=f'get_file_{arquivo}',
        bash_command=f"""{bashcommand} "{bucketname}/{remote_file}" > {local_file} """,
        dag=dag)

    end_log = DummyOperator(
        task_id='end_log',
        dag=dag)

    start_log >> get_file >> end_log