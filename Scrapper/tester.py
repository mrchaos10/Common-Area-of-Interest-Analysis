import os
l1=['1','2','3','4','5']
l2=['1','2','3','6','7']
print list(set(l1)-set(l2))
l1=list(set(l1)-set(l2))
print l1
#print list(set(l2)-set(l1))

l=os.listdir('/home/mrchaos10/Desktop/FriendshipAnalysis/Scrapper/DataSets')
l1=os.listdir('/home/mrchaos10/Desktop/FriendshipAnalysis/Scrapper/TranslatedDataSets')

#already translated datas are subtracted from the original dattasets
l=list(set(l)-set(l1))
print l

