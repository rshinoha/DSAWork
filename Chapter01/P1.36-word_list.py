# Data Structures and Algorithms in Python Ch.1 (Goodrich et. al.)
# Project exercise P1.36
# Ryoh Shinohara
# =======================================================================================
# Write a Python program that inputs a list of words, separated by whitespace, and
# outputs how many times each word appears in the list. You need not worry about
# efficiency at this point, however, as this topic is something that will be addressed
# later in this book.

def getWords():
    """
    Creates a list of lowercased words from stdin
    """
    return [i.lower() for i in input().split()]

def createWordDict(words):
    """
    Given a list of words, generates a word count dictionary
    """
    keys = set(words)
    wordDict = {i: 0 for i in keys}
    for word in words:
        wordDict[word] += 1
    return wordDict

def main():
    print("Type words and press enter:")
    words = getWords()
    wordDict = createWordDict(words)
    print("Word count:")
    for key, value in wordDict.items():
        print("{} = {}".format(key, value))

if __name__ == "__main__":
    main()