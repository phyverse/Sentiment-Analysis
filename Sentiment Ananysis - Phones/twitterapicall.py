import tweepy
from textblob import TextBlob
import sqlite3

class twitterapi(object):
    def __init__(self):
        self.api()
    def api(self):
        consumer_key = 'yourAPIkey'
        consumer_secret = 'your_secret_key'
        access_token = 'your_access_token'
        access_token_secret = 'your_secret_key'
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        api = tweepy.API(auth,wait_on_rate_limit=True)
        public_tweets = api.search('Samsung','iphone','HTC','Redmi','vivo')

        # to store in sqlite database
        def storeInDb(id, tweets, name, polarity, subjectivity):
            conn = sqlite3.connect('tweet.db')
            c = conn.cursor()
            c.execute("INSERT INTO tweetdata VALUES(?,?,?,?,?)", (id, tweets, name, polarity, subjectivity,))
            conn.commit()
            conn.close()

        for tweet in tweepy.Cursor(api.search,q="phone",count=10,result_type="recent",include_entities=True,lang="en").items():
            ids=tweet.id_str
            tweetsO=tweet.text
            tweets=tweetsO.lower()
            analysis = TextBlob(tweet.text)
            pol=analysis.sentiment.polarity
            sub=analysis.sentiment.subjectivity
            print(tweetsO)
            #for Apple
            if "iphone" in tweets or "Apple" in tweets or "ios" in tweets:
                storeInDb(ids,tweetsO,"iphone",pol,sub)
                # print("iphone")


            #for Redmi
            elif "Redmi" in tweets or "Mi" in tweets or "xiaomi" in tweets:
                storeInDb(ids, tweetsO, "Redmi", pol, sub)
                # print("Redmi")


            #for Samsung
            elif "Samsung" in tweets or "Samsung Phones" in tweets or "Samsung Mobiles" in tweets:
                storeInDb(ids, tweetsO, "Samsung", pol, sub)
                #print("Samsung")


            #for HTC
            elif "HTC" in tweets or "htc phone" in tweets or "HTC Mobiles" in tweets or "HTC Smartphones" in tweets:
                storeInDb(ids, tweetsO, "HTC", pol, sub)
                #print("HTC")


            #for vivo
            elif "vivo" in tweets or "vivo camera phone" in tweets or "vivo Mobiles" in tweets or "vivo phones" in tweets:
                storeInDb(ids, tweetsO, "vivo", pol, sub)
                #print("vivo")


            #for other
            else:
                #print("other")
                storeInDb(ids, tweetsO, "Other", pol, sub)



            #print("=========================================")
if __name__ == '__main__':
    twitterapi()
