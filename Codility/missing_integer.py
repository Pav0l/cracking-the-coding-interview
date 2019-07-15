"""
Write a function that, given an array A of N integers,
returns the smallest positive integer (greater than 0) that does not occur in A.

For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.
Given A = [1, 2, 3], the function should return 4.
Given A = [−1, −3], the function should return 1.

Write an efficient algorithm for the following assumptions:
    N is an integer within the range [1..100,000];
    each element of array A is an integer within the range [−1,000,000..1,000,000]
"""


def missing_int(A):
    a = sorted(A)
    first_positive_int = None

    # find first positive int (1) idx
    for i in range(len(a)):
        if a[i] == 1:
            first_positive_int = i
            break

    # it can be 0
    if first_positive_int == None:
        return 1

    # array of only positive integers i > 0
    new_a = a[first_positive_int:]

    for i in range(len(new_a)-1):
        if new_a[i] != new_a[i + 1]:
            if new_a[i] != new_a[i+1] - 1:
                return new_a[i] + 1

    return new_a[-1] + 1


a = [2, 3, -5, 0, 5]
print(missing_int(a))

a = [-2, -3, -5, -8, -5]
print(missing_int(a))

a = []
print(missing_int(a))

a = [2]
print(missing_int(a))

a = [1]
print(missing_int(a))

a = [1, 1, 1]
print(missing_int(a))

a = [-3, -2, 7, 2, 4, 6, 1]
print(missing_int(a))

a = [2, 8, 5, 1, 3, 4, 6, 7, 7, 10, 1]
print(missing_int(a))
