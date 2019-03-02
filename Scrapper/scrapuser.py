#!/usr/bin/env python
import tweepy
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import sys

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

user = api.get_user(sys.argv)
print user.screen_name
print user.description
print user.followers_count
print user.statuses_count
print user.url
print user.id
print user.id_str
print user.location
print user.friends_count
print user.listed_count
print user.favourites_count
print user.created_at
print user.utc_offset
print user.time_zone
print user.geo_enabled
print user.lang
print contributors_enabled
print user.background_color

