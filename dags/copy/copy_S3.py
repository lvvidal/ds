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

from scripts.cleanjson import clean_file

# Airflow Variables
AIRFLOW_HOME = Path(os.environ.get("AIRFLOW_HOME", "~/airflow"))

dag_name = "copy_from_s3"

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
        "local_file": f"{AIRFLOW_HOME}/dags/data/json/nyc_2009.json"
    },
    "extractJSON2010": {
        "bucketname": "https://s3.amazonaws.com/data-sprints-eng-test",
        "bashcommand": "curl -k -X GET",
        "remote_file": "data-sample_data-nyctaxi-trips-2010-json_corrigido.json",
        "local_file": f"{AIRFLOW_HOME}/dags/data/json/nyc_2010.json"
    },
    "extractJSON2011": {
        "bucketname": "https://s3.amazonaws.com/data-sprints-eng-test",
        "bashcommand": "curl -k -X GET",
        "remote_file": "data-sample_data-nyctaxi-trips-2011-json_corrigido.json",
        "local_file": f"{AIRFLOW_HOME}/dags/data/json/nyc_2011.json"
    },
    "extractJSON2012": {
        "bucketname": "https://s3.amazonaws.com/data-sprints-eng-test",
        "bashcommand": "curl -k -X GET",
        "remote_file": "data-sample_data-nyctaxi-trips-2012-json_corrigido.json",
        "local_file": f"{AIRFLOW_HOME}/dags/data/json/nyc_2012.json"
    },
    "extractCSVPayment": {
        "bucketname": "https://s3.amazonaws.com/data-sprints-eng-test",
        "bashcommand": "curl -k -X GET",
        "remote_file": "data-payment_lookup-csv.csv",
        "local_file": f"{AIRFLOW_HOME}/dags/data/csv/nyc_payment.csv"
    },
    "extractCSVVendor": {
        "bucketname": "https://s3.amazonaws.com/data-sprints-eng-test",
        "bashcommand": "curl -k -X GET",
        "remote_file": "data-vendor_lookup-csv.csv",
        "local_file": f"{AIRFLOW_HOME}/dags/data/csv/nyc_vendor.csv"
    }
}

dag = DAG(
    dag_id=dag_name,
    default_args=args,
    catchup=False,
    schedule_interval='30 3 * * *')  # 00:30 GMT-3

#   with open(f'{AIRFLOW_HOME}/dags/copy/copy_s3.md', 'r') as f:
#       dag.doc_md = f.read()

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

def decide_which_path(**context):

    for val in job_info.items():

    for arquivo, val in job_info.items():

        local_file = val['local_file']

        print (local_file)

        if os.path.splitext(local_file)[1] == '.json':
            return "clean_json"         
        else:
            return "clean_csv"


clean_task = BranchPythonOperator(
    task_id='clean_task',
    python_callable=decide_which_path,
    trigger_rule="all_done",
    provide_context=True,
    dag=dag)

clean_json = PythonOperator(
    task_id='clean_json',
    python_callable=clean_file,
    op_kwargs={
        'path': f'{AIRFLOW_HOME}/dags/data/'
    },
    dag=dag)

clean_csv = BashOperator(
    task_id='clean_csv',
    bash_command=f"""sed -i '1d' {AIRFLOW_HOME}/dags/data/csv/nyc_payment.csv""",
    dag=dag)

end_log = DummyOperator(
    task_id='end_log',
    dag=dag)

start_log >> loop_files() >> clean_task >> [clean_json,clean_csv] >> end_log