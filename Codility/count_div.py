"""
Write a function that, given three integers A, B and K,
returns the number of integers within the range [A..B] that are divisible by K, i.e.:

    { i : A ≤ i ≤ B, i mod K = 0 }

Write an efficient algorithm for the following assumptions:
    A and B are integers within the range [0..2,000,000,000];
    K is an integer within the range [1..2,000,000,000];
    A ≤ B.
"""
import math


# O(n)
def count_div(A, B, K):
    count = 0

    if B == 0:
        return 1
    if A == B and A % K == 0:
        return 1

    for i in range(A, B+1):
        if i == 0:
            count += 1
        elif i % K == 0:
            count += 1

    return count


def new_count_div(A, B, K):
    isEven = 0

    if A % K == 0:
        isEven = 1

    return (B-A)//K + isEven


a = 11
b = 345
k = 17
print('expect 20, result: ', new_count_div(a, b, k))


a = 6
b = 6
k = 2
print('expect 1, result: ', new_count_div(a, b, k))

a = 0
b = 6
k = 2
print('expect 4, result: ', new_count_div(a, b, k))

a = 0
b = 0
k = 2
print('expect 1, result: ', new_count_div(a, b, k))


a = 0
b = 14
k = 2
print('expect 8, result: ', new_count_div(a, b, k))

a = 0
b = 13
k = 2
print('expect 7, result: ', new_count_div(a, b, k))
