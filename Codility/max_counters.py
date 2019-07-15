"""
You are given N counters, initially set to 0, and you have two possible operations on them:

increase(X) − counter X is increased by 1,
max counter − all counters are set to the maximum value of any counter.

A non-empty array A of M integers is given. This array represents consecutive operations:

if A[K] = X, such that 1 ≤ X ≤ N, then operation K is increase(X),
if A[K] = N + 1 then operation K is max counter.

For example, given integer N = 5 and array A such that:
    A[0] = 3
    A[1] = 4
    A[2] = 4
    A[3] = 6
    A[4] = 1
    A[5] = 4
    A[6] = 4

the values of the counters after each consecutive operation will be:
    (0, 0, 1, 0, 0)
    (0, 0, 1, 1, 0)
    (0, 0, 1, 2, 0)
    (2, 2, 2, 2, 2)
    (3, 2, 2, 2, 2)
    (3, 2, 2, 3, 2)
    (3, 2, 2, 4, 2)

The goal is to calculate the value of every counter after all operations.

Write a function that, given an integer N and a non-empty array A consisting of M integers,
returns a sequence of integers representing the values of the counters.
"""


# O(n * m)
def max_counter(N, A):
    counter = [0] * N
    max_counter = 0

    for i in range(len(A)):
        if A[i] >= 1 and A[i] <= N:
            idx = A[i] - 1
            counter[idx] += 1
            if counter[idx] > max_counter:
                max_counter = counter[idx]
        else:
            for j in range(len(counter)):
                counter[j] = max_counter

    return counter


def new_max_counter(N, A):
    counter = [0] * N
    max_counter = 0
    last_max_counter = []

    for i in range(len(A)):
        if A[i] >= 1 and A[i] <= N:
            idx = A[i] - 1
            counter[idx] += 1
            if counter[idx] > max_counter:
                max_counter = counter[idx]
        else:
            last_max_counter = [i, max_counter]

    # no max counter opeartions
    if len(last_max_counter) == 0:
        return counter

    new_counter = [last_max_counter[1]] * N
    max_counter = 0
    new_A = A[last_max_counter[0] + 1:]

    for i in range(len(new_A)):
        idx = new_A[i] - 1
        new_counter[idx] += 1
        if counter[idx] > max_counter:
            max_counter = counter[idx]

    return new_counter


n = 5
a = [3, 4, 4, 6, 1, 4, 4]
print(new_max_counter(n, a))


n = 1
a = [1]
print(new_max_counter(n, a))
n = 5
a = [6, 6, 6, 6, 6, 6, 6]
print(new_max_counter(n, a))
