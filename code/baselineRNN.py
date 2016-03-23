#baselineRNN.py
#script designed to hold the functions to initially generate our RNN

#imports

import cPickle
import theano

#load in dataset

def datasetLoadIn(datasetFilename):
    #helper designed to load in our initial dataset
    datasetFile = open(datasetFilename,"rb")
    #three lists of parse trees for different labels
    [liberalSent,conservSent,neutralSent] = cPickle.load(datasetFile)
    return [liberalSent,conservSent,neutralSent]

class neuralNet(
#activation functions

#forward propagation

#generate RNN with dataset

#testing

print datasetLoadIn("../data/full_ibc/ibcData.pkl")[0][0].get_words()