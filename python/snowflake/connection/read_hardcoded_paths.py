import json

def snow_creds():
    with open("/opt/airflow/python/snowflake/connection/snow_creds.json","r") as f: #Modified 8/2/2024
         cred = json.load(f)
         return cred


def paths():
    with open("/opt/airflow/python/snowflake/connection/hardcoded_paths.json","r") as f: #Modified 8/2/2024
         params = json.load(f)
         return params


def aws_creds():
    with open("/opt/airflow/python/snowflake/connection/aws_creds.json","r") as f: #Modified 8/2/2024
         cred = json.load(f)
         return cred



