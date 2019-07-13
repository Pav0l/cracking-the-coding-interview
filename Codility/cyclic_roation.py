"""
An array A consisting of N integers is given.
Rotation of the array means that each element is shifted right by one index,
and the last element of the array is moved to the first place.
For example, the rotation of array A = [3, 8, 9, 7, 6] is [6, 3, 8, 9, 7]
(elements are shifted right by one index and 6 is moved to the first place).

The goal is to rotate array A K times; that is, each element of A will be shifted to the right K times.

Write a function that, given an array A consisting of N integers and an integer K,
returns the array A rotated K times.
"""


def cyclic_rotation(A, K):
    l = len(A)
    new_arr = [None] * l

    if l == 1:
        return A

    for i in range(l):
        new_i = i + K
        if new_i > l - 1:
            new_i = get_i(new_i, l)
        new_arr[new_i] = A[i]

    return new_arr


def get_i(i, l):
    if i > l - 1:
        i = get_i(i-l, l)
    return i


a = [1, 2, 3, 4]
k = 8
print(cyclic_rotation(a, k))
# print(get_i(8, 4, 1))
