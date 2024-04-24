from airflow.models import DAG
from airflow.providers.mysql.operators.mysql import MySqlOperator

from uuid import uuid4
from datetime import datetime, timedelta

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

id = uuid4().__str__()
now = datetime.now().__str__()
default_args = {
    'start_date': datetime.today()
}

with DAG(
    'insert_alarm',
    default_args = default_args,
    description = """
        insert data to 'alarms' table
    """,
    schedule_interval = timedelta(minutes=3),  # scheduler interval 설정
    start_date = datetime(2024, 4, 24),
    catchup = False,    # 과거 실행에서 누락된 작업 재실행 여부
    tags = ['mysql', 'test', 'alarms']
) as dag:
    t2 = MySqlOperator(
        task_id="insert_employees_data",
        mysql_conn_id="mysql",
        sql='insert into `alarms` values ('+id+',`000164ff-ce67-4836-a219-0857d7530e76`, `test_title`, `test_content`, `test_link`, '+now+', '+now+' );'
    )

    t2