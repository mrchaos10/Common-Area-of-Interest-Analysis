#!/usr/bin/env python
# -*- coding: utf-8 -*-
from nltk.corpus import wordnet as wn
from itertools import chain
import os

####################################   THE NLTK CORPUS USAGE #######################################################
    
'''print(syns[0].name())
print(syns[0].lemmas()[0].name())
print(syns[0].definition())
print(syns[0].examples())
for i,j in enumerate(wn.synsets(word)): 
    print('Hypernyms:', ', '.join(list(chain(*[l.lemma_names() for l in j.hypernyms()]))))'''
#########################################    ENDS     ##############################################################     

l=os.listdir('/home/mrchaos10/Desktop/FriendshipAnalysis/Scrapper/PurifiedDataSet')


def read_by_tokens(fileobj):
    for line in fileobj:
        for token in line.split():
            yield token
def check_for_hypernim(token):
    hypernims=[]
    hypernims1 = []
    hypernims2 = []
    hypernims3 = []
    hypernims4 = []
    hypernims5 = []
    hypernims6 = []
    hypernims7 = []
    hypernims8 = []
    hypernims9 = []
    hypernims10 = []
    hypernims11 = []
    hypernims12 = []
    hypernims13 = []
    hypernims14 = []
    hypernims15 = []
    try:
        print(token)
        #1st level hypernims calculation
        try:
           for i,j in enumerate(wn.synsets(token)): 
                 hypernims1=list(chain(*[l.lemma_names() for l in j.hypernyms()]))
        except IndexError:
                 hypernims1=list(token)
        #print(hypernims1) 
        
        #2nd level hypernims calculation
        try:
           for i,j in enumerate(wn.synsets(hypernims1[0])): 
                 hypernims2=list(chain(*[l.lemma_names() for l in j.hypernyms()]))
        except IndexError:
                 hypernims2=hypernims1[0]
        #3rd level hypernims calculation
        try:
           for i,j in enumerate(wn.synsets(hypernims2[0])): 
                hypernims3=list(chain(*[l.lemma_names() for l in j.hypernyms()]))
        except IndexError:
                hypernims3=hypernims2[0]
        #4th level hypernims calculation
        try:
           for i,j in enumerate(wn.synsets(hypernims3[0])): 
                 hypernims4=list(chain(*[l.lemma_names() for l in j.hypernyms()]))
        except IndexError:
                 hypernims4=hypernims3[0]
        #5th level hypernims calculation
        try:
           for i,j in enumerate(wn.synsets(hypernims4[0])): 
                 hypernims5=list(chain(*[l.lemma_names() for l in j.hypernyms()]))
        except IndexError:
                 hypernims5=hypernims4[0]
        #6th level hypernims calculation
        try: 
           for i,j in enumerate(wn.synsets(hypernims5[0])): 
                 hypernims6=list(chain(*[l.lemma_names() for l in j.hypernyms()]))
        except IndexError:
                 hypernims6=hypernims5[0]
        #7th level hypernims calculation
        try:
           for i,j in enumerate(wn.synsets(hypernims6[0])): 
                 hypernims7=list(chain(*[l.lemma_names() for l in j.hypernyms()]))
        except IndexError:
                 hypernims7=hypernims6[0] 
        #8th level hypernims calculation
        try:
           for i,j in enumerate(wn.synsets(hypernims7[0])): 
                 hypernims8=list(chain(*[l.lemma_names() for l in j.hypernyms()]))
        except IndexError:
                 hypernims8=hypernims7[0]
        #9th level hypernims calculation
        try:
           for i,j in enumerate(wn.synsets(hypernims8[0])): 
                 hypernims9=list(chain(*[l.lemma_names() for l in j.hypernyms()]))
        except IndexError:
                 hypernims9=hypernims8[0]
        #10th level hypernims calculation
        try:
           for i,j in enumerate(wn.synsets(hypernims9[0])): 
                 hypernims10=list(chain(*[l.lemma_names() for l in j.hypernyms()]))
        except IndexError:
                 hypernims10=hypernims9[0]
        #11th level hypernims calculation
        try:
           for i,j in enumerate(wn.synsets(hypernims10[0])): 
                 hypernims11=list(chain(*[l.lemma_names() for l in j.hypernyms()]))
        except IndexError:
                 hypernims11=hypernims10[0]
        #12th level hypernims calculation
        try:
           for i,j in enumerate(wn.synsets(hypernims11[0])): 
                 hypernims12=list(chain(*[l.lemma_names() for l in j.hypernyms()]))
        except IndexError:
                 hypernims12=hypernims11[0]
        #13th level hypernims calculation
        try:
           for i,j in enumerate(wn.synsets(hypernims12[0])): 
                 hypernims13=list(chain(*[l.lemma_names() for l in j.hypernyms()]))
        except IndexError:
                 hypernims13=hypernims12[0]
        #14th level hypernims calculation
        try:
           for i,j in enumerate(wn.synsets(hypernims13[0])): 
                 hypernims14=list(chain(*[l.lemma_names() for l in j.hypernyms()]))
        except IndexError:
                 hypernims14=hypernims13[0]
        #15th level hypernims calculation
        try:
           for i,j in enumerate(wn.synsets(hypernims14[0])): 
                 hypernims15=list(chain(*[l.lemma_names() for l in j.hypernyms()]))
        except IndexError:
                 hypernims15=hypernims14[0]
        
        hypernims.append(hypernims1[0])
        hypernims.append(hypernims2[0])
        hypernims.append(hypernims3[0])
        hypernims.append(hypernims4[0])
        hypernims.append(hypernims5[0])
        hypernims.append(hypernims6[0])
        hypernims.append(hypernims7[0])
        hypernims.append(hypernims8[0])
        hypernims.append(hypernims9[0])
        hypernims.append(hypernims10[0])
        hypernims.append(hypernims11[0])
        hypernims.append(hypernims12[0])
        hypernims.append(hypernims13[0])
        hypernims.append(hypernims14[0])
        hypernims.append(hypernims15[0])
        '''
        print('HYPERNIMS ::::::::::::::::::',hypernims)
        
        print('HYPERNIMS2 ::::::::::::::::::',hypernims2[0])
        print('HYPERNIMS3 ::::::::::::::::::',hypernims3[0])
        print('HYPERNIMS4 ::::::::::::::::::',hypernims4[0])
        print('HYPERNIMS5 ::::::::::::::::::',hypernims5[0])
        print('HYPERNIMS6 ::::::::::::::::::',hypernims6[0])
        print('HYPERNIMS7 ::::::::::::::::::',hypernims7[0])
        print('HYPERNIMS8 ::::::::::::::::::',hypernims8[0])
        print('HYPERNIMS9 ::::::::::::::::::',hypernims9[0])
        print('HYPERNIMS10 ::::::::::::::::::',hypernims10[0])
        print('HYPERNIMS11 ::::::::::::::::::',hypernims11[0])
        print('HYPERNIMS12 ::::::::::::::::::',hypernims12[0])
        print('HYPERNIMS13 ::::::::::::::::::',hypernims13[0])
        print('HYPERNIMS14 ::::::::::::::::::',hypernims14[0])
        print('HYPERNIMS15 ::::::::::::::::::',hypernims15[0])'''
        
        #print(set(antonyms))   
    except IndexError:
        hypernims1=list(token)

        
    return hypernims  

for names in l:
    print names
    hype=[]
    with open('PurifiedDataSet/'+names) as f:
        for token in read_by_tokens(f):
            hype=check_for_hypernim(token)
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
               print(hype)
            else:
               print(hype) 
