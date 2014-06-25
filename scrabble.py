#!/usr/bin/env python

'''Scrabble.

Usage:
  scrabble.py <letters>

Options:
  -h --help     Show this message.

'''

from os.path import join, dirname, realpath
from itertools import permutations as permute
from operator import itemgetter
from docopt import docopt

letter_freq = {'e': 12, 'a': 9, 'i': 9, 'o': 8, 'n': 6, 'r': 6,
               't': 6, 'l': 4, 's': 4, 'u': 4, 'd': 4, 'g': 3,
               'b': 2, 'c': 2, 'm': 2, 'p': 2, 'f': 2, 'h': 2,
               'v': 2, 'w': 2, 'y': 2, 'k': 1, 'j': 1, 'x': 1,
               'q': 1, 'z': 1}


letter_values = {'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4,
                 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1,
                 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1,
                 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8,
                 'y': 4, 'z': 10}


def permute_rack(letters):
    perms = []
    for i in range(1, 8):
        perm = permute(letters, i)
        for p in perm:
            # need joining because perm() returns a tuple
            perms.append(''.join(p))
    return perms


def give_possible_words(candidate_words, letters):

    words = join(dirname(realpath(__file__)), 'scrabble_words.txt')
    with open(words, 'r') as f:
        lines = set([line.rstrip('\r\n') for line in f])
        candidate_words = set(candidate_words)
        possible_words = lines & candidate_words

    return possible_words


def score_word(word, letter_values):
    return sum([letter_values[i] for i in word])


def zip_words_and_scores(possible_words, letter_values):

    words_n_scores = []
    for word in possible_words:
        score = score_word(word, letter_values)
        words_n_scores.append((word, score))

    # sort by word score
    return sorted(words_n_scores, key=itemgetter(1), reverse=True)


def print_best_words(words_n_scores):
    for word, score in words_n_scores:
        print score, '\t', word


def main():
    arguments = docopt(__doc__)
    letters = arguments['<letters>']

    candidate_words = permute_rack(letters)
    possible_words = give_possible_words(candidate_words, letters)
    words_n_scores = zip_words_and_scores(possible_words, letter_values)
    print_best_words(words_n_scores)


if __name__ == '__main__':
    main()
