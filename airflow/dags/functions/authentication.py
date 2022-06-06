import tweepy

from functions.keys import keys


def authentication():
        consumer_key,consumer_secret,access_key,access_secret = keys() 
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_key, access_secret)
        return tweepy.API(auth)