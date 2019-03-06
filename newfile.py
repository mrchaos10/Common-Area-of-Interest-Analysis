from os import listdir
from os.path import isfile, join
import csv
import matplotlib.pyplot as plt
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import KNeighborsClassifier, NearestNeighbors
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import pandas as pd

onlyfiles = [f for f in listdir("E:\\Clustering\\Files") if isfile(join("E:\\Clustering\\Files", f))]
print(onlyfiles)

neededfile = input("ENter filename")

onlyfiles.remove(neededfile)
rows = []
y = []
c = 0
for f1 in onlyfiles:
    print(c)
    c+=1
    rows1= []
    with open("E:\\Clustering\\Files\\"+f1, 'r') as csv1:
        # creating a csv reader object
        csvreader1 = csv.reader(csv1)

        f = 0
        # extracting each data row one by one
        for row in csvreader1:
            if f == 0:
                f = 1
                continue

            s = ''
           # print(row)
            for i in range(1,len(row)):

                for j in row[i].split("\n"):
                        #s+=j+" "
                        if j not in rows1:
                            #print(j)
                            rows1.append(j)
                            y.append(row[0])

            del (row[0])
        #print(rows1)
        rows.extend(rows1)
print("done")
vectorizer = TfidfVectorizer(stop_words='english')
X = vectorizer.fit_transform(rows)
from sklearn.cluster import KMeans


modelknn = KNeighborsClassifier(n_neighbors=14)
modelknn.fit(X,y)

f=0
rows=[]

rows1 = []

r2 = []
with open("E:\\Clustering\\Files\\"+neededfile, 'r') as csv1:
    # creating a csv reader object
    csvreader1 = csv.reader(csv1)

    # extracting each data row one by one
    for row in csvreader1:
        if f == 0:
            f = 1
            continue
        #y.append(row[0])

        #del(row[0])
        r = []
       # print(row)
        for i in range(1, len(row)):

            for j in row[i].split("\n"):
                # s+=j+" "
                if j not in rows1:
                    rows1.append(j)


        del (row[0])
print(rows1)
Test = vectorizer.transform(rows1)
predicted_labels_knn = modelknn.predict(Test)
print(predicted_labels_knn)
from collections import Counter

counts = Counter(predicted_labels_knn)
print(counts)


dict = {}
for i in counts:
    dict[i] = []

for i in range(0,len(predicted_labels_knn)):

    dict[predicted_labels_knn[i]].append(rows1[i])
print(dict)
rows1 =[]
fig, ax1 = plt.subplots()
for i in counts:
    vect = vectorizer.fit_transform(dict[i])
    count_vect_df = pd.DataFrame(vect.todense(), columns=vectorizer.get_feature_names())
    print(i)
    f = 0
    for i1 in count_vect_df.shape:
        if i1==1:
            f=1
            break
    if f==1:
        continue
    print(count_vect_df)
    #vals_std = StandardScaler().fit_transform(count_vect_df)
    pca = PCA(n_components=2).fit(count_vect_df)

    data2D = pca.transform(count_vect_df)

    colors = plt.cm.rainbow(np.linspace(0, 1, len(counts)))
    #print(colors)
    #cs = [colors[int(i/len(Test.todense()))] for i in range(len(vectorizer.transform(predicted_labels_knn).todense())*len(Test.todense()))]
    #print(cs)

        #print(vectorizer.transform(i))
        #data = pca1.transform(vectorizer.transform(list(i)).todense())
    x=""
    x+=i
    k =x.replace("_","")
    ax1.scatter(data2D[:,0],data2D[:,1],label=k)
ax1.legend()
plt.show()


