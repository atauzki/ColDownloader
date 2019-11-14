# coding: utf-8

import pickle


def dumpWordList(dicts, fileName):
    print("Saving word lists...")
    with open(fileName, 'wb') as f:
        pickle.dump(dicts, f)


def loadWordList(fileName):
    print("Loading word lists...")
    with open(fileName, 'rb') as f:
        dicts = pickle.load(f)
    return dicts
