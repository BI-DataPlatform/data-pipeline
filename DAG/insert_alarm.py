from airflow.models import DAG
from airflow.providers.mysql.operators.mysql import MySqlOperator
from airflow.operators.python import PythonOperator

from uuid import uuid4
from datetime import datetime, timedelta
import random

default_args = {
    'start_date': datetime.today()
}
id = uuid4().__str__()
now = datetime.now().strftime("%Y-%m-%d %H:%M:%S").__str__()

with DAG(
    'insert_alarm',
    default_args = default_args,
    description = """
        insert data to 'alarms' table
    """,
    schedule_interval = timedelta(minutes=3),  # scheduler interval 설정
    catchup = False,    # 과거 실행에서 누락된 작업 재실행 여부
    tags = ['mysql', 'test', 'alarms']
) as dag:
    
    t1 = MySqlOperator(
        task_id="select_random_account_data",
        mysql_conn_id="mysql",
        sql="SELECT id FROM accounts ORDER BY RAND() LIMIT 1;",
    )


    def print_account_data(**context):
        account_data = context['task_instance'].xcom_pull(task_ids="select_random_account_data", key="return_value")
        print("Random account data:", account_data)

    t2 = PythonOperator(
        task_id="print_account_data",
        python_callable=print_account_data,
        provide_context=True  # context 제공을 위한 옵션
    )

    t3 = MySqlOperator(
        task_id="insert_alarm_data",
        mysql_conn_id="mysql",
        sql="INSERT INTO alarms VALUES ('{}','{{{{ task_instance.xcom_pull(task_ids=\"select_random_account_data\",  key=\"return_value\")[0][0] }}}}', 'test_title', 'test_content', 'test_link', '{}', '{}');".format(id, now, now)
    )

    t1 >> t2 >> t3
    
    
    
    
    
# schema는 mysql cli로 생성
# CREATE TABLE alarms (
# 	id VARCHAR(64) NOT NULL,
# 	account_id VARCHAR(64) NOT NULL,
# 	title VARCHAR(100) NULL,
# 	content VARCHAR(500) NULL,
# 	link VARCHAR(200) NULL,
# 	created_on TIMESTAMP NULL,
# 	last_updated_on TIMESTAMP NULL
# );
# CREATE TABLE favorites (
# 	id	VARCHAR(64)	NOT NULL,
# 	account_id	VARCHAR(64)	NOT NULL,
# 	store_id	VARCHAR(64)	NOT NULL,
# 	created_on	TIMESTAMP NULL,
# 	last_updated_on	TIMESTAMP NULL
# );