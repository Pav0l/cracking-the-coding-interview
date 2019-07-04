"""
Quick Sort I Runtime: 0 (n log (n)) average, 0 (n2) worst case. Memory: 0 (log (n) ) .

In quick sort, we pick a random element and partition the array, such that all numbers that are less than the
partitioning element come before all elements that are greater than it. The partitioning can be performed
efficiently through a series of swaps.

If we repeatedly partition the array (and its sub-arrays) around an element, the array will eventually become
sorted. However, as the partitioned element is not guaranteed to be the median (or anywhere near the
median), our sorting could be very slow. This is the reason for the 0 (n2) worst case runtime.

Algorithm

1. Select a pivot. Often times this is the first or last element in a set. It can also be the middle.
2. Move all elements smaller than the pivot to the left.
3. Move all elements greater than the pivot to the right.
4. While LHS and RHS are greater than 1, repeat steps 1-3 on each side.
"""


def divide(arr):
    # take a pivot point (random element from the array)
    pivot = arr[0]
    left = []
    right = []
    # sort any element lower than pivot to left array
    # and any element higher than pivot to right array
    for i in range(1, len(arr)):
        if arr[i] <= pivot:
            left.append(arr[i])
        else:
            right.append(arr[i])
    # returns a tuple of (left LIST, pivot INT, right LIST)
    return left, pivot, right


# start here
def quick(arr):
    # when the array has more than one element,
    # you want to divide it and sort it to left/right arrays around the pivot
    # and run this function again, until the array contains only single element
    if len(arr) > 1:
        # divide returns a tuple of ([left], pivot, [right])
        left, pivot, right = divide(arr)

        # concat the returned arrays with pivot as an array into one array
        return quick(left) + [pivot] + quick(right)

    # if the array has only one element, return it as it is sorted already
    return arr


print(quick([1, 5, 8, 4, 2, 9, 6, 0, 3, 7]))
