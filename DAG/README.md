- python / mysql / airflow DAG 연동 테스트
- 찜, 알람 테이블 생성

### 설치 패키지

- airflow 패키지
  `pip3 install apache-airflow-providers-mysq`
  - 에러 시 아래 커맨드 순서대로 실행해볼 것. 설치시 mysql config가 필요한 듯 함. \
    `pip install -U pip setuptools` \
    `sudo apt install default-libmysqlclient-dev pkg-config -y` \
    `pip install mysqlclient`
