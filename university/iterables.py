#!/usr/bin/env python3

from itertools import product
from itertools import permutations
from collections import OrderedDict

def match_permutations(string, words:list):
    ''' Find all permutations of a string in list'''
    # permutations as a set
    # {'tac', 'act', 'atc', 'tca', 'cat', 'cta'}
    perms = set(map(''.join, permutations(string)))
    # sorted list of matching strings
    matching_perms =  sorted([ x for x in perms if x in words ])
    return matching_perms


def plur2sing(singular, plural):
    # {'goose':'geese', 'man':'men', 'child':'children'}
    sg2pl = {s: p for s, p in zip(singular, plural)}
    # inversion using zip
    pl2sg = {s: p for s, p in zip(sg2pl.values(),sg2pl.keys())}
    return pl2sg


def vect2word(word2vect):
    v2w =  {tuple(s) : p for p,s in word2vect.items()}
    return v2w


def first_nonrepeating(string: str):
    """ Find first unique character in line"""

    startIndex = ord('!')
    endIndex = ord('~')
    charsList = OrderedDict({chr(char) : 0 for char in range(startIndex, endIndex+1)})
    for char in string:
        charOrd = ord(char)
        if(charOrd > startIndex and charOrd < endIndex):
            charsList[char] += 1

    for key, val in charsList.items():
        if val == 1:
            # print(f"returning key:val = {key}:{val}")
            return key
    return None


def construct_expression(lst: list, answer: int):
    """ Find right placement of parentheses in expression,
    so it will be equal to answer"""

    new_lst = lst[:]
    new_lst = [str(i) for i in new_lst]
    plus_minus = ('+', '-')

    # check if expression without parentheses suits
    try:
        if(eval("".join(new_lst)) == answer):
            return "".join(new_lst)
    except Exception:
        pass

    # check if expression with one short parentheses suits
    for pos, char in enumerate(new_lst):
        if char in plus_minus:
            temp_list = new_lst[:]
            temp_list.insert(pos + 2, ')')
            temp_list.insert(pos - 1, '(')
            try:
                if(eval("".join(temp_list)) == answer):
                    return "".join(temp_list)
            except Exception:
                pass

    # check expression with two short parentheses
    if new_lst[1] in plus_minus and new_lst[5] in plus_minus:
        temp_list = new_lst[:]
        temp_list.insert(7, ')')
        temp_list.insert(4, '(')
        temp_list.insert(3, ')')
        temp_list.insert(0, '(')
        try:
            if(eval("".join(temp_list)) == answer):
                return "".join(temp_list)
        except Exception:
            pass

    # check expression with one long parentheses at the begining
    if new_lst[5] not in plus_minus:
        temp_list = new_lst[:]
        temp_list.insert(5, ')')
        temp_list.insert(0, '(')
        try:
            if(eval("".join(temp_list)) == answer):
                return "".join(temp_list)
        except Exception:
            pass

    # check expression with one long parentheses at the end
    if new_lst[1] not in plus_minus:
        temp_list = new_lst[:]
        temp_list.insert(7, ')')
        temp_list.insert(2, '(')
        try:
            if(eval("".join(temp_list)) == answer):
                return "".join(temp_list)
        # If some exception cathed(e.g. Zero division) return None
        except Exception:
            pass
    # If nothing found return None
    return None


def combine4(numbers: list, answer: int):
    """ Find all combinations of 4 numbers and math basic operations
    to get given answer"""

    signs = list(product("+-*/", repeat=3))
    nums = list(permutations(numbers, 4))

    output_list = []
    for num_list in nums:
        for sign_list in signs:
            tmp_nums = list(num_list)
            for indx, pos in enumerate(range(3, 0, -1)):
                tmp_nums.insert(pos, sign_list[indx])
            temp_answ = construct_expression(tmp_nums, answer)
            if temp_answ is not None:
                output_list.append(temp_answ)
    return sorted(list(set(output_list)))


def test():
    """Test functionality of implemented fucntions"""

    assert match_permutations('act', {'cat', 'rat', 'dog', 'act'}) == ['act', 'cat']
    assert plur2sing(['goose', 'man', 'child'], ['geese', 'men', 'children']) == {'geese': 'goose', 'men': 'man', 'children': 'child'}
    assert sum(k[1] for k in vect2word({'king': [3, 1], 'queen': [6, 3], 'uncle': [4, 3], 'aunt': [8, 9]})) == 16

    assert first_nonrepeating("tooth") == 'h'
    assert first_nonrepeating("lool") is None
    assert first_nonrepeating("\t") is None
    assert first_nonrepeating(" ") is None


if __name__ == '__main__':
    test()
