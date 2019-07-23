"""
https://www.hackerrank.com/challenges/minimum-swaps-2/problem
You are given an unordered array consisting of consecutive integers [1, 2, 3, ..., n] without any duplicates.
You are allowed to swap any two elements.
You need to find the minimum number of swaps required to sort the array in ascending order.
"""


def min_swaps(arr):
    N = len(arr)

    pos = [0] * (N+1)
    swaps = 0

    for i in range(N):
        pos[arr[i]] = i

    for i in range(N):
        if i+1 == arr[i]:
            pass
        else:
            cur_value = arr[i]
            cur_idx_of_value = pos[i+1]

            arr[cur_idx_of_value] = cur_value
            arr[i] = i+1
            pos[i+1] = i
            pos[cur_value] = cur_idx_of_value

            swaps += 1

    return swaps


a = [4, 3, 1, 2]
print(min_swaps(a))
