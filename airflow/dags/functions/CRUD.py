from airflow.providers.postgres.hooks.postgres import PostgresHook




import psycopg2



def connect():
    try:
        pg_hook = PostgresHook(postgres_conn_id = 'postgres_default')
        conn = pg_hook.get_conn()
        return conn
    except psycopg2.Error as e:
        print(f'Erro na conexão ao PostgreSQL Server: {e}')





def desconnect(conn): 
    if conn:
        conn.close()





def insert_database(data):
    conn = connect()
    cursor = conn.cursor()
    author_id = data[0]
    screen_name = data[1]
    followers_count = data[2]
    text_tweet = data[3]
    created_at = data[4]
    hashtag = data[5]

    try:
        cursor.execute(f"INSERT INTO t_user (author_id, screen_name , followers_count) VALUES ('{author_id}','{screen_name}', {followers_count}) ON CONFLICT(author_id) DO UPDATE SET screen_name = EXCLUDED.screen_name, followers_count = EXCLUDED.followers_count ")
        cursor.execute(f"INSERT INTO t_tweet (author_id, text_tweet , created_at) VALUES ('{author_id}','{str(text_tweet)}', '{created_at}') ON CONFLICT(text_tweet) DO UPDATE SET author_id = EXCLUDED.author_id, created_at = EXCLUDED.created_at  ")
        cursor.execute('select id from t_tweet order by id DESC LIMIT 1')
        id_tweet = cursor.fetchall()
        cursor.execute(f"INSERT INTO t_hashtag (id_tweet, hashtag) VALUES ('{id_tweet[0][0]}','{hashtag}')")
    except:
        pass
        
    conn.commit()
    
    desconnect(conn)





def select_all(table_name):
    
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('select count(*) from information_schema.columns where table_name= '+"'"+table_name+"'")
    num_columns =  cursor.fetchall()
    cursor.execute('SELECT column_name FROM INFORMATION_SCHEMA.COLUMNS WHERE table_name ='+"'"+table_name+"'")
    columns_name =  cursor.fetchall()
    cursor.execute('SELECT * FROM '+ table_name)
    hashtags = cursor.fetchall()
    print(columns_name)
    if len(hashtags) > 0:
        print('Fetching all rows...')
        print('-------------------------')
        for hashtag in hashtags:
            for i in range(1,num_columns[0][0]):
                print(columns_name[i][0] ,f': {hashtag[i]}')
            print('-------------------------')
    else: print('empty table')
    desconnect(conn)


# In[ ]:




