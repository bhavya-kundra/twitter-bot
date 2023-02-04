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

# First get the user whose tweets you want to like

user = api.get_user(user_id = 'Enter Your User ID Here')
print(user.screen_name)

# Then get the list of tweets
user_timeline = api.user_timeline(screen_name = user.screen_name, count = 10)
print(user_timeline)

# Then get the recent tweet
user_timeline_status_obj = user_timeline[0]
print(user_timeline_status_obj)

# Then get the id of the recent tweet
status_obj_id = user_timeline_status_obj.id
print("The id of the recent tweet is: " + str(status_obj_id))

# Then get the text of the recent tweet
status_obj = api.get_status(status_obj_id)
print("The text of the recent tweet is: " + status_obj.text)

# Then like the recent tweet
api.create_favorite(status_obj_id)
print('Tweet liked')
