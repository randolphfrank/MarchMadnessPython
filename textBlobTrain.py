from textblob.classifiers import NaiveBayesClassifier

import pickle

neg_tweets = open('../negative_tweets.txt', 'r').read()
pos_tweets = open('../positive_tweets.txt', 'r').read()

train_data = []

neg_tweets = neg_tweets.split(', \"')
pos_tweets = pos_tweets.split(', \"')

max_add = 1000
count = 0

for i in neg_tweets:
    if count <= max_add:
        if 'text\":' in i:
            neg_out = i[8:]
            neg_out = neg_out[:-1]

            sub_array = [neg_out, 'neg']
            train_data.append(sub_array)
            sub_array = []
            count = count + 1

count = 0

for j in pos_tweets:
    if count <= max_add:
        if 'text\":' in j:
            pos_out = j[8:]
            pos_out = pos_out[:-1]

            sub_array = [pos_out, 'pos']
            train_data.append(sub_array)
            sub_array = []
            count = count + 1

# sub_data = train_data[0:50]
# print(sub_data)

# print(train_data)
cl = NaiveBayesClassifier(train_data)

file = open('trainedClassifier.pickle','wb')
pickle.dump(cl,file)
file.close()

print('Finished training')