__authors__ = ['electric-blue']
import math
import sys

tenLetterWords = []

def main(tenLetterWords):
    word = str(input('Enter the word here: '))
    checkWord(word, tenLetterWords)


def checkWord(word, tenLetterWords):
    if word.isnumeric():
        print('Don\'t enter a number, silly!')
        main()
    else:
        countWord(word, tenLetterWords)

def countWord(word, tenLetterWords):
    if len(word) == 10:
        print(word, 'is 10 letters long!')
        addWord(word, tenLetterWords)
    else:
        print(word, 'is not 10 letters long')
        print('All 10 letter words:')
        print(tenLetterWords)
    ask = input('Do another? y/n')
    if ask == 'y' or ask == 'Y':
        main()
    else:
        sys.exit()
def addWord(word, tenLetterWords):
    tenLetterWords.append(word)

main(tenLetterWords)
