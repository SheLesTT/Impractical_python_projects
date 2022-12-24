import loadDictionary

def cleanUp(word_list):

    for word in word_list:
        if len(word) == 1:
            word_list.remove(word)
    return word_list