import json
import pandas as pd
import matplotlib.pyplot as plt
import re
import xlsxwriter
from textClassify import *


dfIn = pd.read_excel("Teams.xlsx")
teamsList = dfIn["Teams"].values.tolist()

def word_in_text(word, text):
    word = word.lower()
    text = text.lower()
    match = re.search(word, text)
    if match:
        return True
    return False

print('Reading Twitter file...')
#read in Twitter input
tweets_data = []
tweet_classification = []
percentPos = []
percentNeg = []

tweets_file = open("twitterStream-out.txt", "r")
for line in tweets_file:
    try:
        tweet = json.loads(line)

        tweets_data.append(tweet)
    except:
        continue

tweets = pd.DataFrame()
tweets['text'] = list(map(lambda tweet: tweet['text'], tweets_data))
tweets['classification'] = tweets['text'].apply(classifyText)
tweets['negative prob'] = tweets['text'].apply(negProb)
tweets['positive prob'] = tweets['text'].apply(posProb)

tweets['lang'] = list(map(lambda tweet: tweet['lang'], tweets_data))
tweets['country'] = list(map(lambda tweet: tweet['place']['country'] if tweet['place'] != None else None, tweets_data))

#relevant tweets only
tweets['relevant'] = tweets['text'].apply(lambda tweet: word_in_text('March Madness', tweet) or word_in_text('NCAA', tweet)
                                          or word_in_text('Basketball', tweet))
#cycle through team list
for team in teamsList:
    try:
        tweets[team] = tweets['text'].apply(lambda tweet: word_in_text(team, tweet))
    except:
        continue

# generate Excel
print('Writing to excel...')
writer = pd.ExcelWriter('sampleOutput.xlsx', engine='xlsxwriter')
tweets.to_excel(writer, sheet_name='Sheet1')
writer.save()
print('Finished')