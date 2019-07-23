"""
https://www.hackerrank.com/challenges/ctci-array-left-rotation/problem
A left rotation operation on an array shifts each of the array's elements unit to the left.
For example, if left 4 rotations are performed on array [1, 2, 3, 4, 5],
then the array would become [5, 1, 2, 3, 4].
"""


def rotLeft(a, d):
    N = len(a)
    new_a = [None] * N

    for i in range(N):
        new_i = i - d
        if new_i < 0:
            new_i = N - d + i

        new_a[new_i] = a[i]

    return new_a


a = [1, 2, 3, 4, 5]
d = 4

rotLeft(a, d)
