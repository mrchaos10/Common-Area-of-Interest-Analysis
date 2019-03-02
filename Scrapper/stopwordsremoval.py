#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize 
import nltk
l=os.listdir('/home/mrchaos10/Desktop/FriendshipAnalysis/Scrapper/EnglishWordsDataSets')
l1=os.listdir('/home/mrchaos10/Desktop/FriendshipAnalysis/Scrapper/PurifiedDataSet')

#already purified datas are subtracted from the english word datasets
l=list(set(l)-set(l1))
#print l


n=0
k=0
def read_by_tokens(fileobj):
    for line in fileobj:
        #for token in line.split():
        yield line

for names in l:
    print n
    print k
    print names
    with open('EnglishWordsDataSets/'+names) as f:
        for token in read_by_tokens(f):
            #print token
            stop_words = set(stopwords.words('english')) 
            word_tokens = word_tokenize(token)
            filtered_sentence = [w for w in word_tokens if not w in stop_words] 
            filtered_sentence = [] 
  
            for w in word_tokens: 
                if w not in stop_words: 
                   filtered_sentence.append(w) 
                #print(word_tokens) 
                tagged = nltk.pos_tag(filtered_sentence)
                for i in tagged:
                    if len(i[0])!=0 or len(i[0])!=1:
                       #print i
                       neuter=0
                       if i[1]=='IN' or i[1]=='DT' or i[1]=='CD' or i[1]=='CC' or i[1]=='EX' or i[1]=='MD' or i[1]=='WDT' or i[1]=='WP' or i[1]=='UH' or i[1]=='TO' or i[1]=='RP' or i[1]=='PDT' or i[1]=='PRP' or i[1]=='PRP$' or i[0]=='co':
                          #print i[1]
                          n=n+1
                          k=k+1
                       else :
                          print i[0] 
                          k=k+1
                          with open('PurifiedDataSet/'+names,"at") as f1:
                               f1.write("%s \n" % i[0].encode("utf-8"))
                 
