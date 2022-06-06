import tweepy
import pandas as pd
import psycopg2
import json

from functions.authentication import authentication
#from functions.CRUD import connect,desconnect,insert,select_all

def scrape(words, date_since, numtweet):
        api = authentication()
        # Creating DataFrame using pandas
 
        # We are using .Cursor() to search
        # through twitter for the required tweets.
        # The number of tweets can be
        # restricted using .items(number of tweets)
        tweets = tweepy.Cursor(api.search_tweets,
                               words + '-filter:retweets AND -filter:replies', lang="pt",
                               since_id=date_since,
                               tweet_mode='extended').items(numtweet)
        
        
        list_tweets = [tweet for tweet in tweets] 
        
        return list_tweets

 