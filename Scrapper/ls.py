import os
import tweepy
import csv
import sys


l=os.listdir('/home/mrchaos10/Desktop/FriendshipAnalysis/Scrapper/DataSets')
li=[x.split('.')[0] for x in l]

for l in li:
    print l
    
