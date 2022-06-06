import json

from functions.CRUD import insert_database

def insert(list_tweets,words):
               
        for tweet in list_tweets:
                author_id = tweet.id
                screen_name = tweet.user.screen_name
                followers_count = tweet.user.followers_count
                created_at = tweet.created_at
                hashtag = words

 
                # Retweets can be distinguished by
                # a retweeted_status attribute,
                # in case it is an invalid reference,
                # except block will be executed
        try:
                text = tweet.retweeted_status.full_text
        except AttributeError:
                text = tweet.full_text
                
        data = author_id, screen_name, followers_count, text, created_at, hashtag
        insert_database(data)