# get_ipython().system('pip install numpy')
# get_ipython().system('pip install scikit-learn')
# get_ipython().system('pip install scipy')
# get_ipython().system('pip install matplotlib')

#install numpy ,scikit-learn,scipy and matplotlib
import sqlite3
from sklearn.cluster import KMeans
import numpy as np
import matplotlib.pyplot as plt


class kmeans(object):
    def __init__(self):
        self.fetch()
        self.process()
        self.graph()
    def fetch(self):
        #get tweets from database
        self.alist=[]
        conn = sqlite3.connect("tweet.db")
        cursor = conn.cursor()
        aaaa=cursor.execute("select polarity,subjectivity,name from tweetdata")
        for lines in aaaa:

            pol=float(lines[0])
            sub=float(lines[1])
            if lines[2]=="Salman Khan":
                name=0
            elif lines[2]=="Aamir Khan":
                name=1
            elif lines[2]=="Shah Rukh Khan":
                name=2
            elif lines[2]=="Saif Ali Khan":
                name=3
            elif lines[2]=="Irrfan Khan":
                name=4
            else :
                name=5
            cordinates=[pol,sub,name]
            self.alist.append(cordinates)
        conn.close()
        # print(alist)

    def process(self):
        #apply keams algorithm
        self.X = np.array(self.alist)

        self.kmeans = KMeans(n_clusters=6, random_state=0).fit(self.X)

        predict=self.kmeans.predict([[0, 0, 0]])
        print("predicted cluster number: "+str(predict))#prints pridicted value

        self.centroids = self.kmeans.cluster_centers_
        self.labels = self.kmeans.labels_
        print("The centroids are: "+str(self.centroids))#prints cluster centerpoint
        print("The lebels are: "+str(self.labels))#prints cluster labels

    def graph(self):
        #ploting in graph
        plt.plot(self.X,'ro')
        plt.ylabel('some numbers')
        plt.show()



        #ploting in scattered chated with color and center point
        colors = ['r','b','y','g','c','m']

        for i in range(len(self.X)):
        #     print("coordinate:",X[i], "label:", labels[i])
            plt.plot(self.X[i][0], self.X[i][1], colors[self.labels[i]], markersize = 10)

        plt.scatter(self.centroids[:, 0],self.centroids[:, 1], marker = "x", s=150, linewidths = 5, zorder = 10)

        plt.show()

        colors = ['r','b','y','g','c','m']
        plt.scatter(self.X[:, 0], self.X[:, 1], color=[colors[l_] for l_ in self.labels], label=self.labels)
        plt.scatter(self.centroids[:, 0],self.centroids[:, 1], color=[c for c in colors[:len(self.centroids)]], marker = "x", s=150, linewidths = 5, zorder = 10)

        plt.show()


if __name__ == '__main__':
    kmeans()
