import tweepy
import twitter_credentials as tc
import datetime
import time


# # AUTH # #

auth = tweepy.OAuthHandler(tc.CONSUMER_KEY, tc.CONSUMER_SECRET)
auth.set_access_token(tc.ACCESS_TOKEN, tc.ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)



#follow = ["realdonaldtrump", "dinoearth_bot"]

#for e in follow:
    #api.create_friendship(e)
    

hour = datetime.datetime.now().hour
minute = datetime.datetime.now(). minute

time = str(hour)l+":"+str(minute)

#print(str(hour)+":"+str(minute))


try:
    print(time)
    if time=="10:29":
        print("10:29")
    else:
        time.sleep(20)
