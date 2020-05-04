import sqlite3
from sklearn.cluster import KMeans
import numpy as np
import csv
class table(object):
    def __init__(self):
        self.generate_tables()
    def generate_tables(self):
        alist = []
        alist2=[]
        self.cluster0=[]
        self.cluster1=[]
        self.cluster2=[]
        self.cluster3=[]
        self.cluster4=[]
        self.cluster5=[]
        conn = sqlite3.connect("tweet.db")
        cursor = conn.cursor()
        aaaa = cursor.execute("select polarity,subjectivity,name,id,tweets from tweetdata")
        for lines in aaaa:

            pol = float(lines[0])
            sub = float(lines[1])
            id=lines[3]
            tweets=lines[4]

            if lines[2] == "Salman Khan":
                name = 0
            elif lines[2] == "Aamir Khan":
                name = 1
            elif lines[2] == "Shah Rukh Khan":
                name = 2
            elif lines[2] == "Saif Ali Khan":
                name = 3
            elif lines[2] == "Irrfan Khan":
                name = 4
            else:
                name = 5
            cordinates = [pol, sub, name]
            cod2=[pol, sub, name,id,tweets]
            alist.append(cordinates)
            alist2.append(cod2)
        conn.close()

        self.X = np.array(alist)

        self.kmeans = KMeans(n_clusters=6, random_state=0).fit(self.X)


        for values in alist2:
            x=values[0]
            y=values[1]
            z=values[2]
            i=values[3]
            t=values[4]
            predict = self.kmeans.predict([[x,y,z]])
            # print(type(predict[0]))
            # print("predicted cluster number: " + str(predict[0])+ " for id ="+ str(i))
            aaa=[x,y,z,i,t]
            if predict[0]==0:
                self.cluster0.append(aaa)
            elif predict[0]==1:
                self.cluster1.append(aaa)
            elif predict[0]==2:
                self.cluster2.append(aaa)
            elif predict[0]==3:
                self.cluster3.append(aaa)
            elif predict[0]==4:
                self.cluster4.append(aaa)
            elif predict[0]==5:
                self.cluster5.append(aaa)

        print("cluster 0---Done")
        with open('cluster0.csv', 'a') as csvfile:
            filewriter = csv.writer(csvfile, delimiter=',',
                                    quotechar='|', quoting=csv.QUOTE_MINIMAL)
            filewriter.writerow(['id', 'name', 'polarity', 'subjectivity', ])
        for items in self.cluster0:
            with open('cluster0.csv', 'a') as csvfile:
                if items[2]==0:
                    khan="Salman Khan"
                elif items[2]==1:
                    khan="Aamir Khan"
                elif items[2]==2:
                    khan="Shah Rukh Khan"
                elif items[2]==3:
                    khan="Saif Ali Khan"
                elif items[2]==4:
                    khan="Irrfan Khan"
                elif items[2]==5:
                    khan="other"
                filewriter = csv.writer(csvfile, delimiter=',',
                                        quotechar='|', quoting=csv.QUOTE_MINIMAL)
                
                filewriter.writerow([items[3],khan,items[0],items[1],])

        print("cluster 1---Done")
        with open('cluster1.csv', 'a') as csvfile:
            filewriter = csv.writer(csvfile, delimiter=',',
                                    quotechar='|', quoting=csv.QUOTE_MINIMAL)
            filewriter.writerow(['id', 'name', 'polarity', 'subjectivity', ])
        for items in self.cluster1:
            if items[2] == 0:
                khan = "Salman Khan"
            elif items[2] == 1:
                khan = "Aamir Khan"
            elif items[2] == 2:
                khan = "Shah Rukh Khan"
            elif items[2] == 3:
                khan = "Saif Ali Khan"
            elif items[2] == 4:
                khan = "Irrfan Khan"
            elif items[2] == 5:
                khan = "other"
            with open('cluster1.csv', 'a') as csvfile:
                filewriter = csv.writer(csvfile, delimiter=',',
                                        quotechar='|', quoting=csv.QUOTE_MINIMAL)

                filewriter.writerow([items[3],khan,items[0],items[1],])
        print("cluster 2---Done")
        with open('cluster2.csv', 'a') as csvfile:
            filewriter = csv.writer(csvfile, delimiter=',',
                                    quotechar='|', quoting=csv.QUOTE_MINIMAL)
            filewriter.writerow(['id', 'name', 'polarity', 'subjectivity', ])
        for items in self.cluster2:
            if items[2] == 0:
                khan = "Salman Khan"
            elif items[2] == 1:
                khan = "Aamir Khan"
            elif items[2] == 2:
                khan = "Shah Rukh Khan"
            elif items[2] == 3:
                khan = "Saif Ali Khan"
            elif items[2] == 4:
                khan = "Irrfan Khan"
            elif items[2] == 5:
                khan = "other"
            with open('cluster2.csv', 'a') as csvfile:
                filewriter = csv.writer(csvfile, delimiter=',',
                                        quotechar='|', quoting=csv.QUOTE_MINIMAL)

                filewriter.writerow([items[3],khan,items[0],items[1],])

        print("cluster 3---Done")
        with open('cluster3.csv', 'a') as csvfile:
            filewriter = csv.writer(csvfile, delimiter=',',
                                    quotechar='|', quoting=csv.QUOTE_MINIMAL)
            filewriter.writerow(['id', 'name', 'polarity', 'subjectivity', ])
        for items in self.cluster3:
            if items[2] == 0:
                khan = "Salman Khan"
            elif items[2] == 1:
                khan = "Aamir Khan"
            elif items[2] == 2:
                khan = "Shah Rukh Khan"
            elif items[2] == 3:
                khan = "Saif Ali Khan"
            elif items[2] == 4:
                khan = "Irrfan Khan"
            elif items[2] == 5:
                khan = "other"
            with open('cluster3.csv', 'a') as csvfile:
                filewriter = csv.writer(csvfile, delimiter=',',
                                        quotechar='|', quoting=csv.QUOTE_MINIMAL)

                filewriter.writerow([items[3],khan,items[0],items[1],])
        print("cluster 4---Done")
        with open('cluster4.csv', 'a') as csvfile:
            filewriter = csv.writer(csvfile, delimiter=',',
                                    quotechar='|', quoting=csv.QUOTE_MINIMAL)
            filewriter.writerow(['id', 'name', 'polarity', 'subjectivity', ])
        for items in self.cluster4:
            if items[2] == 0:
                khan = "Salman Khan"
            elif items[2] == 1:
                khan = "Aamir Khan"
            elif items[2] == 2:
                khan = "Shah Rukh Khan"
            elif items[2] == 3:
                khan = "Saif Ali Khan"
            elif items[2] == 4:
                khan = "Irrfan Khan"
            elif items[2] == 5:
                khan = "other"
            with open('cluster4.csv', 'a') as csvfile:
                filewriter = csv.writer(csvfile, delimiter=',',
                                        quotechar='|', quoting=csv.QUOTE_MINIMAL)

                filewriter.writerow([items[3],khan,items[0],items[1],])
        print("cluster 5---Done")
        with open('cluster5.csv', 'a') as csvfile:
            filewriter = csv.writer(csvfile, delimiter=',',
                                    quotechar='|', quoting=csv.QUOTE_MINIMAL)
            filewriter.writerow(['id', 'name', 'polarity', 'subjectivity', ])
        for items in self.cluster5:
            if items[2] == 0:
                khan = "Salman Khan"
            elif items[2] == 1:
                khan = "Aamir Khan"
            elif items[2] == 2:
                khan = "Shah Rukh Khan"
            elif items[2] == 3:
                khan = "Saif Ali Khan"
            elif items[2] == 4:
                khan = "Irrfan Khan"
            elif items[2] == 5:
                khan = "other"
            with open('cluster5.csv', 'a') as csvfile:
                filewriter = csv.writer(csvfile, delimiter=',',
                                        quotechar='|', quoting=csv.QUOTE_MINIMAL)
                filewriter.writerow([items[3],khan,items[0],items[1],])


if __name__ == '__main__':
    table()
