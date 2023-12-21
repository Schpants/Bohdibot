import nltk
nltk.download('punkt')
from nltk.stem.lancaster import LancasterStemmer
stemmer = LancasterStemmer()
import numpy
import tflearn
import pickle
import random
import json


def bag_of_words(s, words):
    bag = [0 for _ in range(len(words))]

    s_words = nltk.word_tokenize(s)
    s_words = [stemmer.stem(word.lower()) for word in s_words]

    for se in s_words:
        for i, w in enumerate(words):
            if w == se:
                bag[i] = 1
            
    return numpy.array(bag)


def bohdigpt_response(content, model, words, labels, data):

    results = model.predict([bag_of_words(content, words)])
    results_index = numpy.argmax(results)
    tag = labels[results_index]

    for tg in data["intents"]:
        if tg['tag'] == tag:
            responses = tg['responses']

    return random.choice(responses)

def get_model(training, output):
    net = tflearn.input_data(shape=[None, len(training[0])])
    net = tflearn.fully_connected(net, 8)
    net = tflearn.fully_connected(net, 8)
    net = tflearn.fully_connected(net, len(output[0]), activation="softmax")
    net = tflearn.regression(net)

    model = tflearn.DNN(net)
    model.load("BohdiGPT/model.tflearn")

    return model

def read_data():
    objects = []
    with open("BohdiGPT/data.pickle", "rb") as f:
        words, labels, training, output = pickle.load(f)
        return words, labels, training, output


def read_intents():
    with open('BohdiGPT/intents.json', encoding="utf8" ) as file:
        data = json.load(file)
        return data



