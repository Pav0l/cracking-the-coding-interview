"""
A non-empty array A consisting of N integers is given.

A permutation is a sequence containing each element from 1 to N once, and only once.

For example, array A such that:
    A = [3, 2, 1, 4]

is a permutation, but array A such that:
    A = [3, 1, 4]

is not a permutation, because value 2 is missing.

The goal is to check whether array A is a permutation.
Write a function that, given an array A, returns 1 if array A is a permutation and 0 if it is not.
"""


def perm_check(A):
    a = sorted(A)

    for i in range(len(A)):
        if a[i] != i + 1:
            return 0
    return 1
