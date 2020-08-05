# ***************************************************************************
#                       =========== datasprints ================
# Teste Técnico de Engenharia de Dados
# DAG - Copy from S3 - faz o download dos arquivos do s3 para o container.
# Candidato : Luiz Vinicius Izidorio Vidal
# ***************************************************************************

import os
import requests
import sys
from pathlib import Path
from airflow.models import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator, BranchPythonOperator
from airflow.operators.bash_operator import BashOperator
from airflow.models import Variable
from datetime import datetime, timedelta

from scripts.utils import clean_file, json_2_csv, move_load_files

# Airflow Variables
AIRFLOW_HOME = Path(os.environ.get("AIRFLOW_HOME", "~/airflow"))

dag_name = "copy_from_s3"
bucket_name = "data-sprints-candidate-luizvidal"

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
        "local_file": f"{AIRFLOW_HOME}/dags/data/json/nyc_2009.json",
        "csv_file":"nyc_2009.csv",
        "folder_s3": "batch/trips"
    },
    "extractJSON2010": {
        "bucketname": "https://s3.amazonaws.com/data-sprints-eng-test",
        "bashcommand": "curl -k -X GET",
        "remote_file": "data-sample_data-nyctaxi-trips-2010-json_corrigido.json",
        "local_file": f"{AIRFLOW_HOME}/dags/data/json/nyc_2010.json",
        "csv_file":"nyc_2010.csv",
        "folder_s3": "batch/trips"
    },
    "extractJSON2011": {
        "bucketname": "https://s3.amazonaws.com/data-sprints-eng-test",
        "bashcommand": "curl -k -X GET",
        "remote_file": "data-sample_data-nyctaxi-trips-2011-json_corrigido.json",
        "local_file": f"{AIRFLOW_HOME}/dags/data/json/nyc_2011.json",
        "csv_file":"nyc_2011.csv",
        "folder_s3": "batch/trips"
    },
    "extractJSON2012": {
        "bucketname": "https://s3.amazonaws.com/data-sprints-eng-test",
        "bashcommand": "curl -k -X GET",
        "remote_file": "data-sample_data-nyctaxi-trips-2012-json_corrigido.json",
        "local_file": f"{AIRFLOW_HOME}/dags/data/json/nyc_2012.json",
        "csv_file":"nyc_2012.csv",
        "folder_s3": "batch/trips"
    },
    "extractCSVPayment": {
        "bucketname": "https://s3.amazonaws.com/data-sprints-eng-test",
        "bashcommand": "curl -k -X GET",
        "remote_file": "data-payment_lookup-csv.csv",
        "local_file": f"{AIRFLOW_HOME}/dags/data/csv/nyc_payment.csv",
        "csv_file":"nyc_payment.csv",
        "folder_s3": "batch/payment"
    },
    "extractCSVVendor": {
        "bucketname": "https://s3.amazonaws.com/data-sprints-eng-test",
        "bashcommand": "curl -k -X GET",
        "remote_file": "data-vendor_lookup-csv.csv",
        "local_file": f"{AIRFLOW_HOME}/dags/data/csv/nyc_vendor.csv",
        "csv_file":"nyc_vendor.csv",
        "folder_s3": "batch/vendor"
    }
}

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

def loop_files():

    loop_get_files = []

    for arquivo, val in job_info.items():

        bucketname = val['bucketname']
        bashcommand = val['bashcommand']
        remote_file = val['remote_file']
        local_file = val['local_file']

        get_file = BashOperator(
            task_id=f'get_file_{arquivo}',
            bash_command=f"""{AIRFLOW_HOME}/dags/copy/create_folder.sh {local_file} && {bashcommand} "{bucketname}/{remote_file}" > {local_file} """,
            dag=dag)

        loop_get_files.append(get_file)

    return loop_get_files

clean_task = DummyOperator(
    task_id='clean_task',
    dag=dag)

clean_json = PythonOperator(
    task_id='clean_json',
    python_callable=clean_file,
    op_kwargs={
        'path': f'{AIRFLOW_HOME}/dags/data/json'
    },
    dag=dag)

clean_csv = BashOperator(
    task_id='clean_csv',
    bash_command=f"""sed -i '1d' {AIRFLOW_HOME}/dags/data/csv/nyc_payment.csv""",
    dag=dag)

json_to_csv = PythonOperator(
    task_id='json_to_csv',
    python_callable=json_2_csv,
    op_kwargs={
        'path': f'{AIRFLOW_HOME}/dags/data/json'
    },
    dag=dag)

move_files = PythonOperator(
    task_id='move_files',
    python_callable=move_load_files,
    op_kwargs={
        'source': f'{AIRFLOW_HOME}/dags/data/',
        'destination' : f'{AIRFLOW_HOME}/dags/load/'
    },
    dag=dag)

def upload_files():

    up_files = []

    for arquivo, val in job_info.items():

        folder_s3 = val['folder_s3']
        csv_file = val['csv_file']

        upload_to_s3 = BashOperator(
            task_id=f'upload_to_s3_{arquivo}',
            bash_command=f"""{AIRFLOW_HOME}/dags/copy/upload_s3.sh {bucket_name} {folder_s3} {AIRFLOW_HOME}/dags/load {csv_file}""",
            dag=dag)

        up_files.append(upload_to_s3)

    return up_files

remove_old_files = BashOperator(
    task_id='remove_old_files',
    bash_command=f"""rm -rf {AIRFLOW_HOME}/dags/data/""",
    dag=dag)

end_log = DummyOperator(
    task_id='end_log',
    dag=dag)

start_log >> loop_files() >> clean_task >> [clean_json,clean_csv] >> json_to_csv >> move_files >> upload_files() >> remove_old_files >> end_log