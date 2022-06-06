from airflow.models import DAG
from airflow.providers.postgres.operators.postgres import PostgresOperator
from airflow.providers.http.sensors.http import HttpSensor
from airflow.providers.http.operators.http import SimpleHttpOperator
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator


from functions.scrape import scrape
from functions.queries import dataframe_followers_count, dataframe_total_tweets,dataframe_tweets_byday
from functions.insert import insert

from datetime import datetime
import json
from pandas import json_normalize


def search_tweets(**context):
    
    tweets_hashtag_1 = scrape('#jesus','2021-01-01',1)
    tweets_hashtag_2 = scrape('#brasil','2021-01-01',1)
    tweets_hashtag_3 = scrape('#pernambuco','2021-01-01',1)
    
    

    context['task_instance'].xcom_push(key ='tweets_hashtag_1', value = tweets_hashtag_1)
    context['task_instance'].xcom_push(key ='tweets_hashtag_2', value = tweets_hashtag_2) 
    context['task_instance'].xcom_push(key ='tweets_hashtag_3', value = tweets_hashtag_3)

    #return tweet_list

def insert_database(tweets, **context): 
    tweets_hashtag_1 = context['task_instance'].xcom_pull(key='tweets_hashtag_1')
    tweets_hashtag_2 = context['task_instance'].xcom_pull(key='tweets_hashtag_2')
    tweets_hashtag_3 = context['task_instance'].xcom_pull(key='tweets_hashtag_3')

    insert(tweets_hashtag_1,'#jesus')
    insert(tweets_hashtag_2,'#brasil')
    insert(tweets_hashtag_3,'#brasil')

    
    
default_args = {
    'start_date': datetime(2022,1,1), 
}
 


with DAG('main_project', schedule_interval='@daily', 
        default_args = default_args,
        catchup = False) as dag:
    #define tasks/operators
 
    creating_table = PostgresOperator(
        task_id ='creating_table',
        postgres_conn_id="postgres_default",
        sql = 'sql/table_schema.sql'
    )


    search = PythonOperator(
        task_id = 'search_tweets',
        python_callable = search_tweets
        
        
        )

    update = PythonOperator(
        task_id = 'insert_database',
        python_callable =  insert_database,
        provide_context=True,
        op_args = [{'tweet_list'}]
        
        )

    followers_count = PythonOperator(
        task_id = 'followers_count',
        python_callable = dataframe_followers_count
        )

    total_tweets = PythonOperator(
        task_id = 'total_tweets',
        python_callable = dataframe_total_tweets
        )

    tweets_byday = PythonOperator(
        task_id = 'tweets_byday',
        python_callable = dataframe_tweets_byday
        )

    creating_table >> search >> update
    update >> followers_count
    update >> total_tweets
    update >> tweets_byday