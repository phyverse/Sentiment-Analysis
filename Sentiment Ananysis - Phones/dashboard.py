import kmeans,manual,table,twitterapicall,dbCreate

def mainfun():
    a=input("What operation do you want to do? [1]Fetch tweets from twitter. [2]See charts of the tweet. [3]Manual input. [4]show users in cluster table. [5]see database [q] Quit: ")

    if a=='1':
        twitterapicall.twitterapi()
        mainfun()
    elif a=='2':
        kmeans.kmeans()
        mainfun()
    elif a=='3':
        manual.manual()
        mainfun()
    elif a=='4':
        table.table()
        mainfun()
    elif a=='5':
        dbCreate.db()
        mainfun()
    elif a=='q':
        quit()
        mainfun()
    else:
        print("sorry enter again.")
        mainfun()
if __name__ == '__main__':
    mainfun()