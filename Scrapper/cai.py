#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import csv
import collections
from operator import itemgetter

l=os.listdir('/home/mrchaos10/Desktop/FriendshipAnalysis/Scrapper/CSVDATAS')
li=[x.split('.')[0] for x in l]

print"Names in the datasets:"

for names in  li:
    print names
count=0
searchTerm = raw_input("Enter the Name to suggest him friends with common areas of interest")

l1=[]
l1.append(searchTerm)
rem=[]
rem=list(set(li)-set(l1))

wordlist=[]

#search term
with open('CSVDATAS/'+searchTerm+'.csv') as f:
     csvreader1 = csv.reader(f)
     for row in csvreader1:
         del(row[0])
         #print row
	 for i in row:
             if(count<=15):
               count=count+1
               continue
             else:
               for j in i.split():
                   #print j
                   wordlist.append(j)
                   
wordfreq = []
for w in wordlist:
    print w
    wordfreq.append(wordlist.count(w))

#print("String\n" + wordstring +"\n")
#print("List\n" + str(wordlist) + "\n")
#print("Frequencies\n" + str(wordfreq) + "\n")

print("count of words in the users csv \n" + str(zip(wordlist, wordfreq)))

wordlist1=[]

print("ALL OTHER USERS NAMES")
for r in rem:
    print r
    with open('CSVDATAS/'+r+'.csv') as f1:
         csvreader2 = csv.reader(f1)
         for row in csvreader2:
             del(row[0])
	     for i in row:
                 if(count<=15):
                    count=count+1
                    continue
                 else:
                    for j in i.split():
                        #print j
                        wordlist1.append(j)

wordfreq1 = []
for w in wordlist1:
    wordfreq1.append(wordlist1.count(w))


#print("String\n" + wordstring +"\n")
#print("List\n" + str(wordlist1) + "\n")
#print("Frequencies\n" + str(wordfreq1) + "\n")
#print("Pairs\n" + str(zip(wordlist1, wordfreq1)))
finalwords=[]
finalfreq=[]

for i in range(0,len(wordlist1)):
	if wordlist1[i] in wordlist:
		#print wordlist1[i],wordlist[wordlist.index(wordlist1[i])],wordfreq1[i]+wordfreq[wordlist.index(wordlist1[i])]
                finalwords.append(wordlist1[i])
                finalfreq.append(wordfreq1[i]+wordfreq[wordlist.index(wordlist1[i])])

finallist=[]
finallist = collections.OrderedDict.fromkeys(zip(finalwords, finalfreq))
'''for i in range(0,len(finalwords)):
	l = []
	l.append(finalwords[i])
	l.append(finalfreq[i])
	finallist.append(l)
#finallist = tuple(finallist)
#finallist = list(finallist)'''

#print finallist

#print sorted(finallist,key=itemgetter(1),reverse=True)
newlist=[]
newlist=sorted(finallist,key=itemgetter(1),reverse=True)
#print newlist

mlist=[]
llist=[]

for i in range(0,len(newlist)/2):
      mlist.append(newlist[i])

for i in range(len(newlist)/2,len(newlist)):
      llist.append(newlist[i])

print("MOST OOCURING AREAS OF INTEREST")
print(mlist)

print("Least OOCURING AREAS OF INTEREST")
print(llist)


