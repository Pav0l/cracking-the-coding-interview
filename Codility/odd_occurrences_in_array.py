"""
A non-empty array A consisting of N integers is given.
The array contains an odd number of elements, and each element of the array
can be paired with another element that has the same value, except for one element that is left unpaired.
"""


def odd_occurrences(A):
    s = sorted(A)
    skip_next = False
    for i in range(len(s)-1):
        if skip_next:
            skip_next = False
        elif s[i] == s[i+1]:
            skip_next = True
        else:
            return s[i]
    return s[-1]


aa = [2, 2, 3, 3, 4]
print(odd_occurrences(aa))
