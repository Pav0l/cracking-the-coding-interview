"""
Given a 2D Array,

We define an hourglass to be a subset of values with indices falling in this pattern in graphical representation:

a b c
  d
e f g

Calculate the hourglass sum for every hourglass in arr, then print the maximum hourglass sum.

Constrains:
-9 <= arr[i][j] <= 9
0 <= i,j <= 5
"""


# Given the small input size, O(n2) solution will be enough
def hourglassSum(arr):
    # minimum hour glass sum (-9 * 7)
    hrg_sum = -63

    row_len = len(arr[0])
    col_len = len(arr)

    for r in range(row_len):
        for c in range(col_len):
            # sum only for complete hourglass
            # row_len and col_len - 3 => size of hourglass 'square'
            if r <= row_len - 3 and c <= col_len - 3:
                cur_sum = arr[r][c] + arr[r][c+1] + arr[r][c+2] + \
                    arr[r+1][c+1] + arr[r+2][c] + arr[r+2][c+1] + arr[r+2][c+2]

                if cur_sum > hrg_sum:
                    hrg_sum = cur_sum
    return hrg_sum


a = [
    [1, 1, 1, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [1, 1, 1, 0, 0, 0],
    [0, 0, 2, 4, 4, 0],
    [0, 0, 0, 2, 0, 0],
    [0, 0, 1, 2, 4, 0],
]
print(f'Expected output = 19. My output = {hourglassSum(a)}')
