import tweepy
import twitter_credentials as tc
import datetime
import time


# # AUTH # #

auth = tweepy.OAuthHandler(tc.CONSUMER_KEY, tc.CONSUMER_SECRET)
auth.set_access_token(tc.ACCESS_TOKEN, tc.ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

#######

follow = ["2dartonline", "yourpantsu", "pomfclub", "nisopict_bot_k2", "nisopict_bot_kr", "regike_", "rocksylight", "cuteanimegirls_", "acecatgirlbot", "gifsanime_"]

########

while True:
    print(datetime.datetime.today().weekday())
    
    if datetime.datetime.today().weekday() == 0 or datetime.datetime.today().weekday() == 1 or datetime.datetime.today().weekday() == 2 or datetime.datetime.today().weekday() == 3 or datetime.datetime.today().weekday() == 4:
        print(str(datetime.datetime.now().hour)+":"+str(datetime.datetime.now().minute))
        
        if str(datetime.datetime.now().hour)+":"+str(datetime.datetime.now().minute)=="7:0":
            for a in follow:
                api.destroy_friendship(a)
                time.sleep(1)
            print("unfollowed")
            time.sleep(31)
        elif str(datetime.datetime.now().hour)+":"+str(datetime.datetime.now().minute)=="16:0":
            for a in follow:
                api.create_friendship(a)
                time.sleep(1)
            print("unfollowed")
            time.sleep(31)
        else:
            print("not the right time")
            time.sleep(5)
            time.sleep(20)
            
    else:
        print("weekend")
        time.sleep(100)
