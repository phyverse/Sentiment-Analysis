import tweepy
from textblob import TextBlob
import sqlite3

class twitterapi(object):
    def __init__(self):
        self.api()
    def api(self):
        consumer_key = 'sc3CsquYxIb4qivoKFaDMkU9s'
        consumer_secret = '32dGZUZnSvcQqZ3dEwUrkn0at5l3DDGZr3ye4fpGVBDIXnKkW6'
        access_token = '970159915464642560-P2P9v1cJoQ9N0brlDca3qPVqDjdJIc6'
        access_token_secret = 'tJNGEhOLr9Bo9U1ba7q7XLF1y56L4m0LkQLizdmKBVNu1'
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        api = tweepy.API(auth,wait_on_rate_limit=True)
        public_tweets = api.search('Bollywood')

        # to store in sqlite database
        def storeInDb(id, tweets, name, polarity, subjectivity):
            conn = sqlite3.connect('tweet.db')
            c = conn.cursor()
            c.execute("INSERT INTO tweetdata VALUES(?,?,?,?,?)", (id, tweets, name, polarity, subjectivity,))
            conn.commit()
            conn.close()

        for tweet in tweepy.Cursor(api.search,q="Khan",count=10,result_type="recent",include_entities=True,lang="en").items():
            ids=tweet.id_str
            tweetsO=tweet.text
            tweets=tweetsO.lower()
            analysis = TextBlob(tweet.text)
            pol=analysis.sentiment.polarity
            sub=analysis.sentiment.subjectivity
            print(tweetsO)
            #for salman khan
            if "salman khan" in tweets or "salmankhan" in tweets or "salman" in tweets:
                storeInDb(ids,tweetsO,"Salman Khan",pol,sub)
                # print("salman khan")


            #for Irrfan khan
            elif "Irrfan khan" in tweets or "Irrfankhan" in tweets or "Irrfan" in tweets:
                storeInDb(ids, tweetsO, "Irrfan Khan", pol, sub)
                # print("Irrfan khan")


            #for aamir khan
            elif "aamir khan" in tweets or "aamirkhan" in tweets or "aamir" in tweets:
                storeInDb(ids, tweetsO, "Aamir Khan", pol, sub)
                #print("aamir khan")


            #for shah rukh khan
            elif "shah rukh khan" in tweets or "shahrukh khan" in tweets or "shahrukhkhan" in tweets or "shahrukh" in tweets:
                storeInDb(ids, tweetsO, "Shah Rukh Khan", pol, sub)
                #print("shah rukh khan")


            #for saif ali khan
            elif "saif ali khan" in tweets or "saifali khan" in tweets or "saifalikhan" in tweets or "saif" in tweets:
                storeInDb(ids, tweetsO, "Saif Ali Khan", pol, sub)
                #print("saif ali khan")


            #for other khans
            else:
                #print("other")
                storeInDb(ids, tweetsO, "Other", pol, sub)



            #print("=========================================")
if __name__ == '__main__':
    twitterapi()