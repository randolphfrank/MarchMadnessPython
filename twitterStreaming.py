import tweepy
from tweepy import OAuthHandler
import time
import pandas as pd

def getTeams(path):
    dfIn = pd.read_excel(path)
    dfIn["SearchTerm"] = dfIn["Hashtag"] + dfIn["Teams"]
    teamsList = dfIn["SearchTerm"].values.tolist()
    qualifierTerms = ['March Madness', 'NCAA', 'Basketball']
    fullSearchList = teamsList + qualifierTerms
    return fullSearchList

class MyStreamListener(tweepy.StreamListener):
    def on_data(self, data):

        try:
            outputData = open("twitterStream-out.txt", "a")
            outputData.write(data)
            outputData.write('\n')
            outputData.close()
            return True

        except:
            print("Data error")
            time.sleep(2)

    def on_error(self, status_code):
        if status_code == 420:
            # returning False in on_data disconnects the stream
            return False

consumer_key = 'KEY'
consumer_secret = 'Secret'
access_token = 'Token'
access_secret = 'Secret'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)
myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth=api.auth, listener=MyStreamListener())

print('Running stream...')
myStream.filter(track=getTeams("Path"))