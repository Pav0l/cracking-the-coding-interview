"""
A non-empty array A consisting of N integers is given. The consecutive elements of array A represent consecutive cars on a road.

Array A contains only 0s and/or 1s:
    0 represents a car traveling east,
    1 represents a car traveling west.

The goal is to count passing cars. We say that a pair of cars (P, Q), where 0 ≤ P < Q < N, is passing when P is traveling to the east and Q is traveling to the west.

For example, consider array A = [0, 1, 0, 1, 1]
We have five pairs of passing cars: (0, 1), (0, 3), (0, 4), (2, 3), (2, 4).

Write a function that, given a non-empty array A of N integers, returns the number of pairs of passing cars.
The function should return −1 if the number of pairs of passing cars exceeds 1,000,000,000.
"""


def passing_cars(arr):
    N = len(arr)
    total = sum(arr)
    pairs_sum = 0

    if N == 1 or total == 0 or total == N:
        return 0

    for i in range(N):
        if arr[i] == 0:
            pairs_sum += total
        else:
            total -= 1

    if pairs_sum > 1000000000:
        return -1

    return pairs_sum


a = [0, 1, 0, 1, 1]
print(passing_cars(a))

a = [1, 1, 1, 1, 1]
print(passing_cars(a))

a = [0, 0, 0, 0, 0]
print(passing_cars(a))

a = [0]
print(passing_cars(a))

a = [0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0]
print(passing_cars(a))
