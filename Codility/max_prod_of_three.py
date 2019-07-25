"""
A non-empty array A consisting of N integers is given.
The product of triplet (P, Q, R) equates to A[P] * A[Q] * A[R] (0 ≤ P < Q < R < N).

Your goal is to find the maximal product of any triplet.

N is an integer within the range [3..100,000];
each element of array A is an integer within the range [−1,000..1,000].


"""

# Strategy - sort the array, prod last 3 elements

# Edge cases:
# 2 positives and multiple negatives => with one negative, the result will be negative, but with 2 negatives
# the result becomes positive value
# 0 makes result == 0

# at least 2 negatives that their product is higher than second and third highest positive
# [3, 2, 1, -5, -4] => -5 * -4 * 3


# O(n*log n) => sorting
def max_prod(A):
    A.sort(reverse=True)

    first = A[0]
    second = A[1]
    third = A[2]
    last = A[-1]
    second_last = A[-2]

    # sorted from highest to lowest
    # for 3 negative results => you want to product highest values (-1 * -2 etc) A[0] * A[1] * A[2]
    # for 2 negative and 1 positive result => you want to product lowest negative values (-7 * -8) with highest positive A[0] * A[-1] * A[-2]
    # for 1 negative and 2 positive result => you want highest values A[0] * A[1] * A[2]
    # for 3 positive results => you want highest values A[0] * A[1] * A[2]

    if first * second * third > first * last * second_last:
        return first * second * third

    return first * last * second_last


a = [-3, 1, 2, -2, 5, 6]
print(max_prod(a))


a = [-3, 0, 0, -2, 0, 7]
print(max_prod(a))


a = [-3, 4, 7, -2, -8, -7]
print(max_prod(a))

a = [-5, -6, -4, -7, -10]
print(max_prod(a))
