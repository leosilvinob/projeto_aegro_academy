#!/usr/bin/env python
# coding: utf-8

# In[1]:


import tweepy
import pandas as pd
import psycopg2
import pandas.io.sql as psql

from keys import keys
from CRUD import connect,desconnect,insert,select_all
from querys import dataframe_followers_count,dataframe_total_tweets,dataframe_tweets_byday


# In[2]:


def scrape(words, date_since, numtweet):
        consumer_key,consumer_secret,access_key,access_secret = keys() 
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_key, access_secret)
        api = tweepy.API(auth)
        # Creating DataFrame using pandas
        db = pd.DataFrame(columns=['author_id',
                                   'screen_name',
                                   'followers_count',
                                   'created_at',
                                   'hashtag',
                                   'text'])
 
        # We are using .Cursor() to search
        # through twitter for the required tweets.
        # The number of tweets can be
        # restricted using .items(number of tweets)
        tweets = tweepy.Cursor(api.search_tweets,
                               words, lang="pt",
                               since_id=date_since,
                               tweet_mode='extended').items(numtweet)
        list_tweets = [tweet for tweet in tweets]; i =1
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
                insert(data)


# In[3]:


if __name__ == '__main__':
        #consumer_key,consumer_secret,access_key,access_secret = keys() 
        #auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        #auth.set_access_token(access_key, access_secret)
        #api = tweepy.API(auth)
 
        # Enter Hashtag and initial date
         
        hashtag = '#jesus' #input()
        
        date_since = '2022-01-01'
 
        # number of tweets you want to extract in one run
        numtweet = 100
        scrape(hashtag, date_since, numtweet)
        print('\nSucess!') 


# In[3]:


dataframe_tweets_byday()


# In[4]:


dataframe_followers_count()


# In[5]:


dataframe_total_tweets()


# In[13]:


desconnect()


# In[6]:


print(query_followers_count())


# In[11]:


select_all('t_tweet')


# In[ ]:




