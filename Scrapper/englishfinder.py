#!/usr/bin/env python
# -*- coding: utf-8 -*-
import enchant, difflib
import os
import re

d = enchant.Dict("en_US")
l=os.listdir('/home/mrchaos10/Desktop/FriendshipAnalysis/Scrapper/FilteredDataSets')

def read_by_tokens(fileobj):
    for line in fileobj:
        for token in line.split():
            yield token

'''def most_appropriate_word(token):
    #word="prfomnc"
    word=token
    dict= {}
    max=0
    a = set(d.suggest(word))
    for b in a:
       tmp = difflib.SequenceMatcher(None, word, b).ratio();
       dict[tmp] = b
       if tmp > max:
          max = tmp
    print dict[max]
    yield 1'''
i=0
for names in l:
    print names
    with open('FilteredDataSets/'+names) as f:
        for token in read_by_tokens(f):
            if d.check(token) is True:                    
                 print(token)   
                 with open('EnglishWordsDataSets/'+names,"at") as f1:
                      f1.write("%s \n" % token.encode("utf-8"))
                      i=i+1
                      
            '''elif d.check(token) is False:
                #print(token)
                word=token
                dict= {}
                max=0
                a = set(d.suggest(word))
                #print a
                if a is None:
                   #print "NO SUGGESTIONS FOR "
                   #print token
                   k=0 
                else:
                    for b in a:
                        tmp = difflib.SequenceMatcher(None, word, b).ratio();
                        dict[tmp] = b
                        if tmp > max:
                           max = tmp
                    #print dict[max],token'''
print "Written"
print i
print "Successfully"           
