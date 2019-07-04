"""
Check Permutation: Given two strings, write a method to decide if one is a permutation of the
other.
"""
# Assumptions:
# Comparision is case sensitive
# Space is relevant


def isPermutation(first, second):
    # Both strings have to be the same length
    # If they are not, they can not be permutations
    if len(first) != len(second):
        return False

    # two strings are permutations if they are equal if sorted
    return sorted(first) == sorted(second)


print(isPermutation(' asadf', 'fd saa'))
