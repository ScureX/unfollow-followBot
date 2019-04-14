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
    if datetime.datetime.today().weekday() <= 0 and day >= 5:
        print(str(datetime.datetime.now().hour)+":"+str(datetime.datetime.now().minute))
        
        if str(datetime.datetime.now().hour)+":"+str(datetime.datetime.now().minute)=="7:0":
            for a in follow:
                api.destroy_friendship(a)
                time.sleep(1)
                time.sleep(30)
        elif zeit=="16:0":
            for a in follow:
                api.create_friendship(a)
                time.sleep(1)
        else:
            print("not the right time")
            time.sleep(5)
            time.sleep(20)
            
    else:
        print("weekend")
        time.sleep(100)




#cmd = input("f/uf: ")

#if cmd=="f":
#    sec = len(follow)
#    print(sec)
#    for a in follow:
#        api.create_friendship(a)
#        sec = sec-1
#        print(sec)
#        time.sleep(1)
#elif cmd=="uf":
#    sec = len(follow)
#    print(sec)
#    for b in follow:
#        api.destroy_friendship(b)
#        sec = sec-1
#        print(l)
#        time.sleep(1)
#else:
#    print("command doesn't exist")
