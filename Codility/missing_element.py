"""
An array A consisting of N different integers is given.
The array contains integers in the range [1..(N + 1)],
which means that exactly one element is missing.

Your goal is to find that missing element.
"""


def missing(A):
    L = len(A)

    # empty array is missing N+1 => 1
    if L == 0:
        return 1
    elif L == 1:
        # arr with single element is missing either 1 or 2
        if A[0] == 1:
            return 2
        else:
            return 1

    a = sorted(A)

    # if the value of element at index i is not equal to i + 1 => you're missing an element
    for i in range(L):
        if a[i] != i + 1:
            return i + 1

    # if you loop through the array without finding the missing element
    # the last element N + 1 is missing
    return a[-1] + 1
