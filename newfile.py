from os import listdir
from os.path import isfile, join
import csv

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import KNeighborsClassifier

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
                            rows1.append(j)
                            y.append(row[0])

            del (row[0])
        #print(rows1)
        rows.extend(rows1)
vectorizer = TfidfVectorizer(stop_words='english')
X = vectorizer.fit_transform(rows)

modelknn = KNeighborsClassifier(n_neighbors=1)
modelknn.fit(X,y)

f=0
rows=[]
y=[]
rows1 = []
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
        s = ''
       # print(row)
        for i in range(1, len(row)):

            for j in row[i].split("\n"):
                # s+=j+" "
                if j not in rows1:
                    rows1.append(j)
                    y.append(row[0])

        del (row[0])

Test = vectorizer.transform(rows1)
predicted_labels_knn = modelknn.predict(Test)
print(predicted_labels_knn)
from collections import Counter

counts = Counter(predicted_labels_knn)
print(counts)
