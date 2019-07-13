"""
Binary gap within a positive integer N is any maximal sequence of consecutive zeros
that is surrounded by ones at both ends in the binary representation of N.

For example, number 9 has binary representation 1001 and contains a binary gap of length 2.
"""


def binary_gap(N):
    n = bin(int(N))
    curr_sum = 0
    temp_max = 0

    for i in range(2, len(n)):
        if n[i] == '0':
            curr_sum += 1
        if n[i] == '1':
            if temp_max < curr_sum:
                temp_max = curr_sum
            curr_sum = 0

    return temp_max


print(binary_gap(328))
