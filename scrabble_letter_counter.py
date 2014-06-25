#!/usr/bin/env python
'''Scrabble tile counter.

Usage:
  scrabble_letter_counter.py add <tiles>
  scrabble_letter_counter.py remove <tiles>
  scrabble_letter_counter.py count

'''

from docopt import docopt
from os.path import join, dirname, realpath


def get_tiles(tiles_path):
    with open(tiles_path, 'a+') as f:
        f.seek(0)
        return f.read()


def add_tiles(tiles_path, tiles_to_add):
    with open(tiles_path, 'a') as f:
        f.write(tiles_to_add)


def remove_tiles(tiles_path, all_tiles, tiles_to_remove):
    new_tiles = all_tiles.translate(None, tiles_to_remove)
    with open(tiles_path, 'w') as f:
        f.write(new_tiles)


def calculateOdds(letter, letter_freq, num_all):
    return float(letter_freq[letter]) / float(num_all)


def getLetterFrequencies(tiles_on_board):
    letter_freq = {'e': 12, 'a': 9, 'i': 9, 'o': 8, 'n': 6, 'r': 6, 't': 6,
                   'l': 4, 's': 4, 'u': 4, 'd': 4, 'g': 3, 'b': 2, 'c': 2,
                   'm': 2, 'p': 2, 'f': 2, 'h': 2, 'v': 2, 'w': 2, 'y': 2,
                   'k': 1, 'j': 1, 'x': 1, 'q': 1, 'z': 1}

    tiles_on_board = tiles_on_board.replace(' ', '')

    for i in tiles_on_board:
        letter_freq[i] = letter_freq[i] - 1

    num_all = sum(x for x in letter_freq.itervalues())
    num_vovels = sum([letter_freq[x] for x in letter_freq if x in 'aeiuoy'])

    print '\n', num_all, 'tiles left'
    print float(num_vovels)/float((num_all)) * 100, 'percent are vovels'

    for k in sorted(letter_freq, key=letter_freq.get, reverse=True):
        if letter_freq[k] > 0:
            odds = round(calculateOdds(k, letter_freq, num_all))
            print k, '\t', odds, 4*100, '\t', '*' * letter_freq[k]


def main():
    arguments = docopt(__doc__)
    tiles_path = join(dirname(realpath(__file__)), 'word_count.txt')
    all_tiles = get_tiles(tiles_path)
    current_tiles = arguments['<tiles>']

    if arguments['add'] is True:
        add_tiles(tiles_path, current_tiles)

    elif arguments['remove'] is True:
        remove_tiles(tiles_path, all_tiles, current_tiles)

    elif arguments['count'] is True:
        getLetterFrequencies(all_tiles)


if __name__ == '__main__':
    main()
