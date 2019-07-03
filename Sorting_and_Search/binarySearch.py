"""
# Binary search

Binary search has a precondition - the list that is being searched **is already sorted**.

Steps to binary search:

Compare the item in the middle of the data set to the item we are searching for.

- If it is the same, stop. We found it and are done!

- Else, if the item we are searching for is LESS than the item in the middle:

- Eliminate the RHS of list. Repeat step 1 with only the LHS of list.

- Else, the item we are searching for is GREATER than the item in the middle:

- Eliminate the LHS of list. Repeat step 1 with only the RHS of the list.
"""

a = [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 18, 21, 32, 65, 78, 145]
t = 65


def binary_search_rec(arr, target):
    # O(1)
    mid_idx = len(arr) // 2
    mid_val = arr[mid_idx]

    # O(1)
    # end conditions: found the target or not found the target
    if mid_val == target:
        return mid_val
    elif len(arr) <= 1:
        return 'Target not found'

    # O(log n)
    # splits - if target less than mid, get rid of right hand side of array
    if mid_val > target:
        return binary_search_rec(arr[:mid_idx], target)
    else:
        return binary_search_rec(arr[mid_idx+1:], target)


print(binary_search_rec(a, t))


def binary_search_iter(arr, target):

    # arr len will be halved every run
    # first step = n/2, 2nd step = n/4, ... 1
    # O(log n)
    while len(arr) >= 1:
        # All operations inside while loop have O(1) time complexity
        mid_idx = len(arr) // 2
        mid_val = arr[mid_idx]

        if mid_val == target:
            return mid_val
        elif mid_val > target:
            arr = arr[:mid_idx]
        else:
            arr = arr[mid_idx+1:]

    return 'Target not found'


print(binary_search_iter(a, t))
