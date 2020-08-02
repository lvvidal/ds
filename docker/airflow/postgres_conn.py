import psycopg2

conn = psycopg2.connect(
    "dbname='airflow' user='airflow' host='postgres' password='airflow'")
