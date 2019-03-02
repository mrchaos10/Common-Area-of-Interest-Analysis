#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import re
import enchant
d = enchant.Dict("en_US")
from googletrans import Translator
translator = Translator()



l=os.listdir('/home/mrchaos10/Desktop/FriendshipAnalysis/Scrapper/DataSets')
l1=os.listdir('/home/mrchaos10/Desktop/FriendshipAnalysis/Scrapper/TranslatedDataSets')

#already translated datas are subtracted from the original datasets
l=list(set(l)-set(l1))
#print l

#li=[x.split('.')[0] for x in l]
def read_by_tokens(fileobj):
    for line in fileobj:
        #for token in line.split():
        yield line

for names in l:
    print names
    with open('DataSets/'+names) as f:
        for token in read_by_tokens(f):
            #print(token)
            with open('TranslatedDataSets/'+names, "at") as f1:
                if d.check(token) is False:
                   #print(token)
                   try:
                      #print(token)
                      print translator.translate(token).text
                      #print("\n\n\n")
                      newtxt=translator.translate(token).text
                      f1.write("%s \n" % newtxt.encode("utf-8"))
            
                  
                   except Exception:
                          pass
               
                elif d.check(token) is True:
                     #print(token)
                     print translator.translate(token).text
                     newtxt=translator.translate(token).text
                     f1.write("%s \n" % newtxt.encode("utf-8"))
            
              
