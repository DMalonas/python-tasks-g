import itertools
from random import randrange


def permutations(iterable, r=None):
    pool = tuple(iterable)
    n = len(pool)
    r = n if r is None else r
    for indices in itertools.product(range(n), repeat=r):
        if len(set(indices)) == r:
            yield tuple(pool[i] for i in indices)


def pushWordsToList(file):
    words = []
    with open(file, 'r') as f:
        for line in f:
            for word in line.split():
                words.append(word)
    return words


def getTuple(z, word):
    for entry in z:
        if entry[0] == word:
            return list(entry)


def checkLength(li):
    if len(li) >= 200:
        return True
    return False


def getRandomText(z):
    jointList = []
    idx = randrange(len(z))
    for word in z:
        w2 = word[len(word) - 2]
        w3 = word[len(word) - 1]
        w2T = getTuple(z, w2)
        w3T = getTuple(z, w3)
        jointList.append(w2)
        if checkLength(jointList):
            return jointList
        jointList.append(w3)
        if checkLength(jointList):
            return jointList
        jointList.extend(w2T)
        if checkLength(jointList):
            return jointList
        jointList.extend(w3T)
        if checkLength(jointList):
            return jointList
    return jointList


def getRandomTextFromFile(file):
    words = pushWordsToList(file)
    z = list(permutations(words, len(words)))
    print(list(z))
    return getRandomText(z)
