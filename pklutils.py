# coding: utf-8

import pickle


def dumpWordList(dicts: str, fileName: str):
    print("Saving word lists...")
    with open(fileName, 'wb') as f:
        pickle.dump(dicts, f)


def loadWordList(fileName: str) -> dict:
    print("Loading word lists...")
    with open(fileName, 'rb') as f:
        dicts = pickle.load(f)
    return dicts
