__authors__ = ['electric-blue']
import math
import sys

def main():
    word = str(input('Enter the word here: '))
    checkWord(word)


def checkWord(word):
    if word.isnumeric:
        print('Don\'t enter a number, silly!')
        main()
    else:
        countWord(word)

def countWord(word):
    if len(word) == 10:
        print(word, 'is 10 letters long!')
    else:
        print(word, 'is not 10 letters long')
    ask = input('Do another? y/n')
    if ask == 'y' or ask == 'Y':
        main()
    else:
        sys.exit()
