"""
https://www.hackerrank.com/challenges/crush/problem
Starting with a 1-indexed array of zeros and a list of operations,
for each operation add a value to each of the array element between two given indices, inclusive.
Once all operations have been performed, return the maximum value in your array.
"""


# O(n * m)
def arr_manip(n, queries):
    arr = [0] * n
    m = len(queries)

    for i in range(m):
        start = queries[i][0] - 1
        end = queries[i][1]
        k = queries[i][2]

        for j in range(start, end):
            arr[j] += k

    return max(arr)


# O(m)
def arr_manip_optimized(n, queries):
    m = len(queries)
    arr = [0] * (n+1)

    for i in range(m):
        start = queries[i][0] - 1
        end = queries[i][1]
        k = queries[i][2]

        arr[start] += k
        arr[end] -= k

    maxv = 0
    count = 0

    for i in arr:
        count += i
        if count > maxv:
            maxv = count

    return maxv


n = 10
q = [
    [1, 5, 3],
    [4, 8, 7],
    [6, 9, 1],
]
print(arr_manip_optimized(n, q))
