import tweepy
import twitter_credentials as tc
import datetime
import time


# # AUTH # #

auth = tweepy.OAuthHandler(tc.CONSUMER_KEY, tc.CONSUMER_SECRET)
auth.set_access_token(tc.ACCESS_TOKEN, tc.ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)



follow = ["2dartonline", "yourpantsu", "pomfclub", "nisopict_bot_k2", "nisopict_bot_kr", "regike_", "rocksylight", "cuteanimegirls_", "acecatgirlbot"]

cmd = input("f/uf: ")

if cmd=="f":
    for a in follow:
        api.create_friendship(a)
        time.sleep(1)
elif cmd=="uf":
    for b in follow:
        api.destroy_friendship(b)
        time.sleep(1)
else:
    print("command doesn't exist")


hour = datetime.datetime.now().hour
minute = datetime.datetime.now(). minute

time = str(hour)+":"+str(minute)

#print(str(hour)+":"+str(minute))



#print(time)
#if time=="11:29":
   # print("now")
   

