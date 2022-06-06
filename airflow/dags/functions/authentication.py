import tweepy


from airflow.models import Variable

def authentication():
        consumer_key = Variable.get('consumer_key')
        consumer_secret = Variable.get('consumer_secret')
        access_key = Variable.get('access_key')
        access_secret = Variable.get('access_secret')

        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_key, access_secret)
        return tweepy.API(auth)