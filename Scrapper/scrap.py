#!/usr/bin/env python
import tweepy

consumerKey = "cGj3ajfw6GeS4MuIFeXfa8oqt"
consumerSecret = "IPMjTnfhjKah675ab9ErIP1blJ7AkroTBCU07oOSPI0vIWrOTz"
accessToken = "940948925351170048-IgKkyEKI3wScSGRmbeHVX74BFudyvw3"
accessTokenSecret = "Nn6uWTH20Mk9knWmnVy9R2DoyffdLROt8jwvwSceV39eU"

auth = tweepy.OAuthHandler(consumerKey,consumerSecret)

auth.set_access_token(accessToken,accessTokenSecret)

api = tweepy.API(auth)

public_tweets = api.followers_ids()
print(api.followers_ids())
print(public_tweets)

for tweet in public_tweets:
    print len(public_tweets)
