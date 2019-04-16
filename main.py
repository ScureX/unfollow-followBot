import tweepy
import twitter_credentials as tc
import datetime
import time


# # AUTH # #

auth = tweepy.OAuthHandler(tc.CONSUMER_KEY, tc.CONSUMER_SECRET)
auth.set_access_token(tc.ACCESS_TOKEN, tc.ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

#######
#array with accounts that should be followed/unfollowed
follow = []

########

while True:
    print(datetime.datetime.today().weekday())

    #checks if its running on a weekday
    if datetime.datetime.today().weekday() == 0 or datetime.datetime.today().weekday() == 1 or datetime.datetime.today().weekday() == 2 or datetime.datetime.today().weekday() == 3 or datetime.datetime.today().weekday() == 4:
        print(str(datetime.datetime.now().hour)+":"+str(datetime.datetime.now().minute))
        
        if str(datetime.datetime.now().hour)+":"+str(datetime.datetime.now().minute)=="7:0":                #destroys friendships at 7am
            for a in follow:
                api.destroy_friendship(a)
                time.sleep(1)
            print("unfollowed")
            time.sleep(31)
        elif str(datetime.datetime.now().hour)+":"+str(datetime.datetime.now().minute)=="16:0":             #creates friendships at 4pm
            for a in follow:
                api.create_friendship(a)
                time.sleep(1)
            print("unfollowed")
            time.sleep(31)
        else:
            print("not the right time")
            time.sleep(25)
            
    else:
        print("weekend")
        time.sleep(300)
