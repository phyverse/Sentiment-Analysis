import sqlite3
class db(object):
    def __init__(self):
        self.database()

    def database(self):
        conn = sqlite3.connect('tweet.db')
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS tweetdata (
                         id integer ,
                         tweets text,
                         name text ,
                         polarity text,
                         subjectivity text);''')
        # cursor.execute("INSERT INTO tweetdata VALUES(?,?,?,?,?)",
        #                ("aaa", "aaa","aaa", "aaa","aaa",))
        # conn.commit()
        # cursor.execute('delete from tweetdata')
        # conn.commit()
        aaaa=cursor.execute("select * from tweetdata ")
        for lines in aaaa:
            print(lines)
        conn.close()

if __name__ == '__main__':
    db()