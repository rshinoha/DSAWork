# Data Structures and Algorithms in Python Ch.1 (Goodrich et. al.)
# Project exercise P1.34
# Ryoh Shinohara
# =======================================================================================
# A common punishment for school children is to write out a sentence multiple times.
# Write a Python stand-alone program that will write out the following sentence one
# hundred times: “I will never spam my friends again.” Your program should number each of
# the sentences and it should make eight different random-looking typos.
from random import randrange

# Number of sentences we want to generage
indexEnd = 100
# Number of errors we want to make
numRand = 8
# Sentence to print
sentence = "I will never spam my friends again."
# Unicode integer for 'a'
a = ord('a')
# Unicode integer for 'z'
z = ord('z')

def randIndexes(indexEnd, numRand):
    """
    Given a stop value for randrange(), generates numRand number of
    different indexes within the range
    """
    indexList = []
    i = numRand
    while i > 0:
        randIndex = randrange(indexEnd)
        if len(indexList) == 0 or randIndex not in indexList:
            indexList.append(randIndex)
        i -= 1
    return indexList

def makeTypo(sentence):
    """
    Given a sentence, generates a new sentence with a random typo
    """
    # Index in sentence to make error
    randIndex = randrange(len(sentence))
    # Letter to use
    randLetter = sentence[randIndex]
    while randLetter == sentence[randIndex]:
        randLetter = chr(randrange(a, z+1))
    newSentence = sentence[:randIndex] + randLetter + sentence[randIndex + 1:]
    return newSentence

def main():
    indexes = randIndexes(indexEnd, numRand)
    for i in range(indexEnd):
        if i in indexes:
            print(makeTypo(sentence))
        else:
            print(sentence)

if __name__ == "__main__":
    main()