"""
Write a function that, given an array A consisting of N integers,
returns the number of distinct values in array A.
"""


# Create a set from the list (set has only unique values)
# the length of the set gives us number of disctinct values
def distinct(A):
    return len(set(A))
