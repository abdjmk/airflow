import sys
sys.path.append('/root/airflow/snowpythconn/')
from creds import make_snowflake_connection as snowcnt

cur= snowcnt.connect_snowflake()



