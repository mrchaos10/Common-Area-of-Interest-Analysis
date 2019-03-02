#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import re
import time
from googletrans import Translator
translator = Translator()



l=os.listdir('/home/mrchaos10/Desktop/FriendshipAnalysis/Scrapper/DataSets')

#li=[x.split('.')[0] for x in l]
def read_by_tokens(fileobj):
    for line in fileobj:
        #for token in line.split():
        yield line
i=0
list1=[]
for names in l:
    print names
    with open('DataSets/'+names,"r") as f:
        for token in read_by_tokens(f):
            print("""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""------------------------""")
            #print(token)
            #print filter(None,re.split(r'RT|\W|\d|^https?:\/\/.*[\r\n]*|^http?:\/\/.*[\r\n]*|https.*|http.*', token))
            
            #key=re.sub(r'^https?:\/\/.*[\r\n]*', '', token, flags=re.MULTILINE)
            #print key
            with open('FilteredDataSets/'+names,"at") as f1:
                 list1=filter(None,re.split(r'[0-9]+|RT|\W|\d|^https?:\/\/.*[\r\n]*|^http?:\/\/.*[\r\n]*|https|http',token))
                 str1 = ' '.join(str(e) for e in list1)
                 f1.write("%s \n" % str1.encode("utf-8"))
                 i=i+1
        #time.sleep(1000)
print("\nSUCCESSFULLY WRITTEN")
print(i)
print("Files")

