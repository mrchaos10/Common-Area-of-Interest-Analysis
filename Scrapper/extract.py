#!/usr/bin/env python
# -*- coding: utf-8 -*-
from nltk.corpus import wordnet as wn
from itertools import chain
import os
import csv

####################################   THE NLTK CORPUS USAGE #######################################################
    
'''print(syns[0].name())
print(syns[0].lemmas()[0].name())
print(syns[0].definition())
print(syns[0].examples())
for i,j in enumerate(wn.synsets(word)): 
    print('Hypernyms:', ', '.join(list(chain(*[l.lemma_names() for l in j.hypernyms()]))))'''
#########################################    ENDS     ##############################################################     

l=os.listdir('/home/mrchaos10/Desktop/FriendshipAnalysis/Scrapper/PurifiedDataSet')
li=[x.split('.')[0] for x in l]


def read_by_tokens(fileobj):
    for line in fileobj:
        for token in line.split():
            yield token

def check_for_hypernim(token):
    hypernims=[]
    for i in range(15):
        try:
           hypernims1=[]
           for i,j in enumerate(wn.synsets(token)): 
                 #hypernims1=list(chain(*[l.lemma_names() for l in j.hypernyms()]))
                 for l in j.hypernyms():
                     hypernims1.append(l.lemma_names()[0])
                 #print token
                 #print(hypernims1)
                 #print(hypernims1[0])
           token=hypernims1[0]
           hypernims.append(hypernims1) 
        except IndexError:
           hypernims.append([token])

        
    return hypernims  

for names in li:
    print names
    hype=[]
    with open('CSVDATAS/'+names+'.csv', 'at') as csv_file:
         filewriter = csv.writer(csv_file, delimiter=',')
         filewriter = csv.writer(csv_file)
         filewriter.writerow(['Screen Name', 'Word', 'Hypernim[1]' , 'Hypernim[2]','Hypernim[3]','Hypernim[4]','Hypernim[5]','Hypernim[6]','Hypernim[7]','Hypernim[8]','Hypernim[9]','Hypernim[10]','Hypernim[11]','Hypernim[12]','Hypernim[13]','Hypernim[14]', 'Hypernim[15]']) 
         with open('PurifiedDataSet/'+names+'.txt') as f:
             for token in read_by_tokens(f):
                 hype=check_for_hypernim(token)
                 print(token)
                 if len(hype)==0:
                    hype.append(token) #1
                    hype.append(token) #2
                    hype.append(token) #3
                    hype.append(token) #4
                    hype.append(token) #5
                    hype.append(token) #6
                    hype.append(token) #7
                    hype.append(token) #8
                    hype.append(token) #9
                    hype.append(token) #10
                    hype.append(token) #11
                    hype.append(token) #12
                    hype.append(token) #13
                    hype.append(token) #14
                    hype.append(token) #15
                    #print(hype)
                 else:
                    hide=0
                    #print(hype)
                 storer=[]
                 storer.append(names)
                 storer.append(token)
                 for hypers in hype:
                     print(hypers)
                     #for hypevariables in hypers:
                          #print(hypevariables)
                     stringer="\n".join(hypers)  
                     storer.append(stringer)
                 shotlist=[]
                 #name already appended in hype
                 #shotlist.append(names)
                 for storage in storer: 
                     #filewriter.writerow()
                     #print(storage.encode('utf-8').strip())
                     shotlist.append(storage.encode('utf-8').strip()) 
                 print(shotlist)
                 filewriter.writerow(shotlist)
