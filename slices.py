#!/usr/bin/env python3

import collections

# for task 1, 2, 3
eskymo = ['do', 'pre', 'du', 'du', 'do', 'za', 'du', 'du']


def distStrings():
    ''' number of all distinct strings in the eskymo list '''
    vocabulary_size_eskymo = len(set(eskymo))

    return vocabulary_size_eskymo


def bothStringsDist():
    # for the next test
    prepos = ['do', 'za', 'pred']

    # all distinct strings in both the lists
    in_both_eskymo_prepos = set(eskymo) & set(prepos)
    in_both_str = ';'.join(in_both_eskymo_prepos)
    return in_both_str


def countStrings():
    # what strings and how many times appeared in the eskymo list
    wordfreq_eskymo = {key : eskymo.count(key) for key in eskymo }
    return ''.join(word+str(freq) for (word, freq) in wordfreq_eskymo.items())


def cropAndRevert(cropLen:int):
    # for the next test
    udubutubudu = 'u dubu tu budu.'

    # the udubutubudu string without the last character, backwards
    backward_except_last = udubutubudu[-(cropLen+1)::-1]
    return backward_except_last


def splitAndJoin():
    # for the next test
    hymnString = 'Hymn of St. John: Ut queant laxis re sonare fibris mi ra gestorum fa muli tuorum sol ve polluti la bii reatum SI Sancte Iohannes'

    # list from string, starting from the fifth string, skipping always two strings
    hymnList = hymnString.split()[4::3]
    # the skip2 list as a string, ', ' as a separator
    skip2Str = ', '.join(hymnList)
    return skip2Str

def test():
    assert distStrings() == 4
    tempStr = bothStringsDist()
    assert (tempStr  == 'do;za' or tempStr == 'za;do')
    assert countStrings() == 'do2pre1du4za1'
    assert cropAndRevert(1) == 'udub ut ubud u'
    assert splitAndJoin() == 'Ut, re, mi, fa, sol, la, SI'

if __name__ == '__main__':
    test()
