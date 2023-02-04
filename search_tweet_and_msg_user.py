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

# First get the list of users with same interest where q is the interest
users_with_same_interests = api.search_users(q='#python', lang='en', result_type='recent')
recipient_id = [users.id for users in users_with_same_interests]
print(recipient_id)
users_name = [users.screen_name for users in users_with_same_interests]
print(users_name)

# Then send the message to the user who has the same interest
api.send_direct_message(recipient_id = recipient_id[0], text = "Hello, I am using Twitter API to send you a message")
time.sleep(5)
print('Message send to user id: ' + str(recipient_id))
