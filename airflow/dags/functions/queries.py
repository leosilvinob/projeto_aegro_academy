import psycopg2
import pandas.io.sql as psql

from functions.CRUD import connect,desconnect

def dataframe_followers_count():
    conn = connect()
    dataframe = psql.read_sql('SELECT t_user.id, t_user.screen_name,t_user.followers_count FROM t_user ORDER BY t_user.followers_count DESC LIMIT 5;', conn)
    desconnect(conn)
    return dataframe.to_csv('followers_count.csv')

def dataframe_total_tweets():
    conn = connect()
    dataframe = psql.read_sql('SELECT COUNT(t_hashtag.id_tweet) AS Total_tweets, t_hashtag.hashtag FROM t_hashtag GROUP BY t_hashtag.hashtag;', conn)
    desconnect(conn)
    return dataframe.to_csv('queries/total_tweets.csv')

def dataframe_tweets_byday():
    conn = connect()
    dataframe = psql.read_sql('SELECT COUNT(t_tweet.id) AS Total_tweets, t_tweet.created_at FROM t_tweet GROUP BY t_tweet.created_at ORDER BY t_tweet.created_at ASC;', conn)
    desconnect(conn)
    return dataframe.to_csv('queries/tweets_by_day.csv',index = False)