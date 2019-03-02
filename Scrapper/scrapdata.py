#!/usr/bin/env python
import tweepy
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener

ckey = 'ckey'
csecret = 'csecret'
atoken = 'tok'
asecret = 'atok'

class Listener(StreamListener):

    def on_data(self, data):
        print data
        return True

    def on_error(self, status_code):
        print status_code

consumerKey = "cGj3ajfw6GeS4MuIFeXfa8oqt"
consumerSecret = "IPMjTnfhjKah675ab9ErIP1blJ7AkroTBCU07oOSPI0vIWrOTz"
accessToken = "940948925351170048-IgKkyEKI3wScSGRmbeHVX74BFudyvw3"
accessTokenSecret = "Nn6uWTH20Mk9knWmnVy9R2DoyffdLROt8jwvwSceV39eU"

auth = tweepy.OAuthHandler(consumerKey,consumerSecret)

auth.set_access_token(accessToken,accessTokenSecret)
api = tweepy.API(auth)

#twitterStream = Stream(auth, Listener())
#twitterStream.filter(track=["car"])
#twitterStream.sample()

users = []

count = 1

searchTerm = raw_input("Enter the keyword/Hashtag to search about:")

numsearchTerm = int(raw_input("Enter how many tweets to be analyzed for sentiments"))

for tweet in tweepy.Cursor(api.search, q=searchTerm).items(numsearchTerm):
#ding thru all tweets and extract the name of non-duplicate

    print "Name:", tweet.author.name.encode('utf8')
    print "Tweet created:", tweet.created_at
    user = tweet.author.screen_name.encode('utf8')
    print user
    print "//////////////////"
    if not users.__contains__(user):
        users.append(user)
    count += 1
    print count

##########################################################################
#while True:
#    try:
#        tweet = c.next()
#        # Insert into db
#    except tweepy.TweepError:
#        time.sleep(60 * 15)
#        continue
#    except StopIteration:
#        break
###########################################################################
print '====================List of unique users in total' + str(len(users))
for u in users:
    print u
    filename = u
    filename += ".txt"
    for status in tweepy.Cursor(api.user_timeline, screen_name=u, tweet_mode="extended").items():
        try:
            f= open(filename, "at")
            s= status.full_text
            print s 
            f.write("%s\n" % s.encode("utf-8"))
            f.close()
        except tweepy.TweepError:
            time.sleep(60 * 15)
            continue
print('done')
