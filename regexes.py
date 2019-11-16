#!/usr/bin/env python3

import re

def getTriplets(animals):
    """
    Return a list of triples containing either a word not followed by (P...)
    and two empty strings, or an empty string, and a word followed by (P...)
    followed, potentially, by the words in the parenthesis
    """
    word_parse = re.compile(r''' (?:(\w+)\s*         \(P(?::?\s*([^)]+))?\) )|
                                 (?:(\w+)(?:\s+|$)(?!\(P         [^)]*   \)))
                             ''', re.X)

    return [(w4actual, w4prev, p_clues_str) for (w4prev, p_clues_str, w4actual) in word_parse.findall(animals)]


def second_task(condensed):
    """
    Replace all . or , by spaces when they are between words
    """
    punct = re.compile(r''' (?<=[^\d][,.])  # after a full stop or comma
                            (?=[^\d])       # ...
                           ''', re.X)

    return punct.sub(' ', condensed)


def test():
    assert getTriplets('bee(P: insect honey) dog  cat (P:milk) ant(P) ape') == \
    [('', 'bee', 'insect honey'), ('dog', '', ''), ('', 'cat', 'milk'), ('', 'ant', ''), ('ape', '', '')]
    assert second_task('Hello,John.I bought 192.168.0.1 for 100,000 bitcoins') == \
    'Hello, John. I bought 192.168.0.1 for 100,000 bitcoins'

if __name__ == '__main__':
    test()
