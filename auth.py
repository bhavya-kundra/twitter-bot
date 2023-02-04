import tweepy
import time
import webbrowser


consumer_key = "Enter Your Consumer Key Here"
consumer_secret = "Enter Your Consumer Secret Here"
access_token = "Enter Your Access Token Here"
access_token_secret = "Enter Your Access Token Secret Here"


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

me = api.verify_credentials()

print(me.screen_name)

redirect_url = 'https://twitter.com/' + me.screen_name

