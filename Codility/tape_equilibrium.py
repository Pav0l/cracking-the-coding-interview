"""
A non-empty array A consisting of N integers is given.
Array A represents numbers on a tape.

Any integer P, such that 0 < P < N, splits this tape into two non-empty parts:
A[0], A[1], ..., A[P − 1] and A[P], A[P + 1], ..., A[N − 1].

The difference between the two parts is the value of:
|(A[0] + A[1] + ... + A[P − 1]) − (A[P] + A[P + 1] + ... + A[N − 1])|

In other words, it is the absolute difference between the sum of the first part
and the sum of the second part.

Write a function that, given a non-empty array A of N integers,
returns the minimal difference that can be achieved.

- N is an integer within the range [2..100,000];
- each element of array A is an integer within the range [−1,000..1,000].

"""


# O(n*n) because sum is O(n) and it's called inside `for` loop
def tape_equilibrium(A):
    N = len(A)
    absolutes = set()

    for P in range(0, N):
        a1 = sum(A[:P])
        a2 = sum(A[P:])
        res = abs(a1 - a2)
        absolutes.add(res)

    return min(absolutes)


# get absolute value from subtracting the first element and sum of the rest of elements
# keep it as min_sum
# loop through the array increasing the left array and decreasing the right arra
# check if their abs is less then min_sum, if yes update min_sum
# at the end return min_sum
# O(n) time complexity
def tape_eq(A):
    N = len(A)
    left = A[0]
    right = sum(A[1:])
    min_sum = abs(left - right)

    for i in range(1, N-1):
        left += A[i]
        right -= A[i]
        cur_sum = abs(left - right)

        if cur_sum < min_sum:
            min_sum = cur_sum

    return min_sum


a = [-10, 10]
print(tape_eq(a))
# 20

a = [3, 1, 2, 4, 3]
print(tape_eq(a))
# 1

a = [1, 1, 3]
print(tape_eq(a))
# 1

a = [1, 3]
print(tape_eq(a))
# 2
