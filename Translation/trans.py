import os

l=os.listdir('/home/mrchaos10/Desktop/FriendshipAnalysis/Scrapper/DataSets')
#li=[x.split('.')[0] for x in l]

for names in l:
    print names
    with open(names) as f:
        for token in read_by_tokens(f):
            print(token)

