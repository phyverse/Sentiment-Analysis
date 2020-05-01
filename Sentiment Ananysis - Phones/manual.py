import sqlite3
from sklearn.cluster import KMeans
import numpy as np


class manual(object):
    def __init__(self):
        self.entry()
    def entry(self):
        po=input("Enter the value of polarity[-1 to 1]: ")
        su=input("Enter the value of subjectivity[0 to 1]: ")
        phone=input("Enter the Phone: ")
        phone=phone.lower()
        if phone == "iphone":
            vsl = 0
        elif phone == "Redmi":
            vsl = 1
        elif phone == "Samsung":
            vsl = 2
        elif phone == "HTC":
            vsl = 3
        elif phone == "Vivo":
            vsl = 4
        else:
            vsl = 5

        alist = []
        conn = sqlite3.connect("tweet.db")
        cursor = conn.cursor()
        aaaa = cursor.execute("select polarity,subjectivity,name from tweetdata")
        for lines in aaaa:

            pol = float(lines[0])
            sub = float(lines[1])


            if lines[2] == "iphone":
                name = 0
            elif lines[2] == "Redmi":
                name = 1
            elif lines[2] == "Samsung":
                name = 2
            elif lines[2] == "HTC":
                name = 3
            elif lines[2] == "Vivo":
                name = 4
            else:
                name = 5
            cordinates = [pol, sub, name]

            alist.append(cordinates)

        conn.close()

        self.X = np.array(alist)

        self.kmeans = KMeans(n_clusters=6, random_state=0).fit(self.X)
        predict = self.kmeans.predict([[po, su, vsl]])

        print("it belongs to cluster "+ str(predict[0])+".")
if __name__ == '__main__':
    manual()
