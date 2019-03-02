import os
import tweepy
import csv
import sys
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener

ckey = 'ckey'
csecret = 'csecret'
atoken = 'tok'
asecret = 'atok'

output_file ='users.csv' 

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

l=os.listdir('/home/mrchaos10/Desktop/FriendshipAnalysis/Scrapper/DataSets')
li=[x.split('.')[0] for x in l]

for names in li:
    print names

with open(output_file, 'wb') as csv_file:
     filewriter = csv.writer(csv_file, delimiter=',')
     filewriter = csv.writer(csv_file)
     filewriter.writerow(['Screen Name', 'Description', 'Followers_count' , 'Statuses_count','URL','Id','Id_str','Location','Friends_count','Listed_count','Favourties_count','Created_At','UTC_offset','Time_zone','Geo_Enabled_Status','Language']) 
     for names in li:
         user = api.get_user(names)
         print user.screen_name
         print user.description
         print user.followers_count
         print user.statuses_count
         print user.url
         print user.id
         print user.id_str
         print user.location
         print user.friends_count
         print user.geo_enabled
         print user.listed_count
         print user.favourites_count
         print user.created_at
         print user.utc_offset
         print user.time_zone
         print user.lang 
         listt=[]
         listt.append(user.screen_name.encode('utf-8').strip())
         listt.append(user.description.encode('utf-8').strip())
         listt.append(user.followers_count)
         listt.append(user.statuses_count)
         listt.append(user.url)
         listt.append(user.id)
         listt.append(user.id_str.encode('utf-8').strip())
         listt.append(user.location.encode('utf-8').strip())
         listt.append(user.friends_count)
         listt.append(user.listed_count)
         listt.append(user.favourites_count)
         listt.append(user.created_at)
         listt.append(user.utc_offset)
         listt.append(user.time_zone)
         listt.append(user.geo_enabled)
         listt.append(user.lang.encode('utf-8').strip())
         for k in listt:
             if k is None:
                k=' '    
         print listt
         filewriter.writerow(listt)

