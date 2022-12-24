import sys
import pprint
import json
from string import punctuation
from nltk.corpus import cmudict


cmudict = cmudict.dict()

def main():
    haiku = load_haiku('train_txt')
    exceptions = cmudict_missing(haiku)
    build_dict = input('\n Build word dictionary by hands (y/n) ? \n ')
    if build_dict.lower() == 'n'
        sys.exit()
    else:
        missing_words_dict = make_exceptions_dict(exceptions)
        save_exceptions(missing_words_dict)

def load_haiku(filename):
    with open(filename) as in_file:
        haiku = set(in_file.read().replace('-',' ').split())
    return haiku

def cmudict_missing(word_set):

    exceptions = set()
    for word in word_set:
        word = word.lower().strip(punctuation)
