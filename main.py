import tweepy
import twitter_credentials as tc
import datetime
import time


# # AUTH # #

auth = tweepy.OAuthHandler(tc.CONSUMER_KEY, tc.CONSUMER_SECRET)
auth.set_access_token(tc.ACCESS_TOKEN, tc.ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

#######

day = datetime.datetime.today().weekday()
hour = datetime.datetime.now().hour
minute = datetime.datetime.now(). minute
time = str(hour)+":"+str(minute)


follow = ["2dartonline", "yourpantsu", "pomfclub", "nisopict_bot_k2", "nisopict_bot_kr", "regike_", "rocksylight", "cuteanimegirls_", "acecatgirlbot", "gifsanime_"]

########


cmd = input("f/uf: ")

if cmd=="f":
    l = len(follow)
    print(l)
    for a in follow:
        api.create_friendship(a)
        l = l-1
        print(l)
        time.sleep(1)
elif cmd=="uf":
    l = len(follow)
    print(l)
    for b in follow:
        api.destroy_friendship(b)
        l = l-1
        print(l)
        time.sleep(1)
else:
    print("command doesn't exist")


  

