import pickle
import time

pickle_in = open("trainedClassifier.pickle", "rb")
print("Loading text classifier...")
cl = pickle.load(pickle_in)
print("Finished loading text classifier\n")
time.sleep(1)

def classifyText(text):
    prob_dist = cl.prob_classify(text)
    classification = prob_dist.max()

    return classification

def negProb(text):
    prob_dist = cl.prob_classify(text)
    probNeg = round(prob_dist.prob("neg"), 2)
    return probNeg

def posProb(text):
    prob_dist = cl.prob_classify(text)
    probPos = round(prob_dist.prob("pos"), 2)
    return probPos