from airflow.decorators import dag, task
from airflow.models.baseoperator import chain
from time import sleep
from airflow.utils.dates import days_ago

@dag(
    schedule=None,
    start_date=days_ago(1),
    catchup=False
)
def parallel_dag():
    @task
    def task_1():
        sleep(30)

    @task
    def task_2():
        sleep(30)

    @task
    def task_3():
        sleep(30)
        
    @task
    def task_4():
        print('Done')

    chain([task_1(), task_2(), task_3()], task_4())

parallel_dag()
