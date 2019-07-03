"""
Merge Sort I Runtime: O( n log (n) ) average and worst case. Memory: Depends.

Merge sort divides the array in half, sorts each of those halves, and then merges them back together. Each
of those halves has the same sorting algorithm applied to it. Eventually, you are merging just two singleelement
arrays. It is the "merge" part that does all the heavy lifting.

The merge method operates by copying all the elements from the target array segment into a helper array,
keeping track of where the start of the left and right halves should be (helperLeft and helperRight).
We then iterate through helper, copying the smaller element from each half into the array. At the end, we
copy any remaining elements into the target array.
"""


def merge(l, r):
    new_ar = []
    for _ in range(len(l) + len(r)):
        if len(l) == 0:
            new_ar += r
            r = []
        elif len(r) == 0:
            new_ar += l
            l = []
        elif l[0] < r[0]:
            a = l.pop(0)
            new_ar.append(a)
        elif r[0] < l[0]:
            b = r.pop(0)
            new_ar.append(b)
    return new_ar


def divide(arr):
    mid_idx = len(arr) // 2
    # array with len == 1 => sorted array
    # split arr until it is 'sorted'
    if len(arr) > 1:
        left = divide(arr[:mid_idx])
        right = divide(arr[mid_idx:])
        # then merge the left and right arr together in a sorted arr
        arr = merge(left, right)
    return arr


print(divide([1, 5, 8, 4, 2, 9, 6, 0, 3, 7]))
