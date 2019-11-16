#!/usr/bin/env python3
import collections


def can_be_a_set_member_or_frozenset(item):
    """Check if item can be a part of set e.g. has HASH"""

    # check if item has HASH
    if isinstance(item, collections.Hashable):
        return item
    else:
        return frozenset(item)


def all_subsets(lst):
    """Return all subsets (with empty set) of given list"""

    # create start list with empty set
    subsets = [[]]
    # iterate through all items in given list
    for item in lst:
        temp_subsets = []
        # construct all possible sets of member of input list
        for mem in subsets:
            if item not in mem:
                # create copy to not change the original member
                mem_cpy = mem[:]
                mem_cpy.append(item[:])
                temp_subsets.append(mem_cpy)
        # add temporary constructed subsets to final list of subsets
        subsets += temp_subsets

    return subsets


def all_subsets_excl_empty(*lst, exclude_empty=True):
    """Return all subsets (with or without empty set) of given parameters"""

    # create start list with empty set
    subsets = [[]]
    # iterate through all arguments
    for item in lst:
        temp_subsets = []
        # construct all possible sets of member of input list
        for mem in subsets:
            if item not in mem:
                # create copy to not change the original member
                mem_cpy = mem[:]
                mem_cpy.append(item[:])
                temp_subsets.append(mem_cpy)
        # add temporary constructed subsets to final list of subsets
        subsets += temp_subsets

    # delete empty set from final list if needed
    if exclude_empty:
        subsets = subsets[1:]
    return subsets


def test():
    """Test functionality of implemented functions"""
    assert can_be_a_set_member_or_frozenset(1) == 1
    assert can_be_a_set_member_or_frozenset((1, 2)) == (1, 2)
    assert can_be_a_set_member_or_frozenset([1, 2]) == frozenset([1, 2])
    assert all_subsets(['a', 'b', 'c']) == [[], ['a'], ['b'], ['a', 'b'], ['c'], ['a', 'c'], ['b', 'c'], ['a', 'b', 'c']]
    assert all_subsets_excl_empty('a', 'b', 'c') == [['a'], ['b'], ['a', 'b'], ['c'], ['a', 'c'], ['b', 'c'], ['a', 'b', 'c']]
    assert all_subsets_excl_empty('a', 'b', 'c', exclude_empty=True) == [['a'], ['b'], ['a', 'b'], ['c'], ['a', 'c'], ['b', 'c'], ['a', 'b', 'c']]
    assert all_subsets_excl_empty('a', 'b', 'c', exclude_empty=False) == [[], ['a'], ['b'], ['a', 'b'], ['c'], ['a', 'c'], ['b', 'c'], ['a', 'b', 'c']]


if __name__ == '__main__':
    test()
