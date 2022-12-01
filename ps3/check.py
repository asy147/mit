import math
import random
import string

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': \
8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': \
1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
    }

WORDLIST_FILENAME = "words.txt"
VOWELS = 'aeiou'

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """

    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print("  ", len(wordlist), "words loaded.")
    return wordlist

word_list = load_words()

def getpts(word,n):
    word = word.lower()
    points = {}
    for letter in word:
        points[letter] = SCRABBLE_LETTER_VALUES[letter]
    check = 7*len(word) - 3*(n-len(word))
    print("check = ", check)
    if check <= 1:
        return 1
    else:
        letter_sum = 0
        for letter in word:
            letter_sum += points[letter]
        print("letter sum = ",letter_sum)
        return letter_sum * check

#print("\"\"","total points",getpts("",7))
#print("it n=7","total points",getpts("it",7))

def upd_hand(hand, word):
    new_hand = hand.copy
    print(type(new_hand))
    for letter in word:
        print(letter)
        if letter in hand:
#            new_hand.pop(aletter)
            pass
    return new_hand


#print(upd_hand({'b': 2, 'd': 3, 'c': 2, 'e': 4},"abd"))

def is_valid_word(word, hand, word_list):
    """
    Returns True if word is in the word_list and is entirely
    composed of letters in the hand. Otherwise, returns False.
    Does not mutate hand or word_list.

    word: string
    hand: dictionary (string -> int)
    word_list: list of lowercase strings
    returns: boolean
    """
    word = word.lower()
    if word in word_list:
        for letter in word:
            if letter not in hand: return False, "a"
            elif word.count(letter) > hand[letter]: return False, "b"

    elif "*" in word:
        wild = word.find("*")
        w1 = word[0:wild]
        w2 = word[wild + 1: len(word)]
        for letter in word:
            if letter not in hand: return False,"c"
            if word.count(letter) > hand[letter]: return False, "d"
            if letter == "*":
                for vowel in VOWELS:
                    print(w1 + vowel + w2)
                    if w1 + vowel + w2 in word_list:
                        return True
                    else: return False, "f"
    else: #here means word not in list and no * letter
        return False
    return True

#print("e*m", is_valid_word("e*m",{'a': 1, 'r': 1, 'e': 1, 'j': 2, 'm': 1, '*': 1}, word_list))
print("h*ney", is_valid_word("h*ney",{'n': 1, 'h': 1, '*': 1, 'y': 1, 'd': 1, 'w': 1, 'e': 2}, word_list))
