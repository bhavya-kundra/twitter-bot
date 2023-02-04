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
user_id = [users.id for users in users_with_same_interests]
print(user_id)
users_name = [users.screen_name for users in users_with_same_interests]
print(users_name)

# Then creating the friendship with the user who has the same interest
api.create_friendship(user_id = user_id[0])
time.sleep(5)
print('Friendship created with user id: ' + str(user_id))
