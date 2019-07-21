"""
A DNA sequence can be represented as a string consisting of the letters A, C, G and T,
which correspond to the types of successive nucleotides in the sequence.
Each nucleotide has an impact factor, which is an integer. Nucleotides of types A, C, G and T
have impact factors of 1, 2, 3 and 4, respectively. You are going to answer several queries of the form:
What is the minimal impact factor of nucleotides contained in a particular part of the given DNA sequence?

The DNA sequence is given as a non-empty string S = S[0]S[1]...S[N-1] consisting of N characters.

There are M queries, which are given in non-empty arrays P and Q, each consisting of M integers.

The K-th query (0 ≤ K < M) requires you to find the minimal impact factor of nucleotides
contained in the DNA sequence between positions P[K] and Q[K] (inclusive).

Write a function that, given a non-empty string S consisting of N characters and two non-empty arrays P and Q consisting of M integers,
returns an array consisting of M integers specifying the consecutive answers to all queries.

Result array should be returned as an array of integers.

Write an efficient algorithm for the following assumptions:

    N is an integer within the range [1..100,000];
    M is an integer within the range [1..50,000];
    each element of arrays P, Q is an integer within the range [0..N − 1];
    P[K] ≤ Q[K], where 0 ≤ K < M;
    string S consists only of upper-case English letters A, C, G, T.
"""


# O(n * m)
def genomic_query(S, P, Q):
    M = len(P)

    values = {'A': 1, 'C': 2, 'G': 3, 'T': 4}

    result = []
    min_impact = 4

    for K in range(M):
        sequence = S[P[K]: Q[K]+1]

        for i in sequence:
            if min_impact > values[i]:
                min_impact = values[i]

        result.append(min_impact)

        min_impact = 4

    return result


# O(n + m)
def genomic_query_two(S, P, Q):
    N = len(S)
    M = len(P)

    # create arrays for every nucleotide
    # that will keep track of prefix sums of nucleotides in DNA sequence
    # N + 1, to start with initial value of 0
    a_prefix_sum = [0] * (N + 1)
    c_prefix_sum = [0] * (N + 1)
    g_prefix_sum = [0] * (N + 1)
    t_prefix_sum = [0] * (N + 1)

    # get prefix sums for each nucleotide
    for i in range(N):
        # update next value with previous value
        a_prefix_sum[i + 1] = a_prefix_sum[i]
        c_prefix_sum[i + 1] = c_prefix_sum[i]
        g_prefix_sum[i + 1] = g_prefix_sum[i]
        t_prefix_sum[i + 1] = t_prefix_sum[i]

        # check which nucleotide is in sequence next and increase its count
        if S[i] == 'A':
            a_prefix_sum[i+1] = a_prefix_sum[i] + 1
        elif S[i] == 'C':
            c_prefix_sum[i+1] = c_prefix_sum[i] + 1
        elif S[i] == 'G':
            g_prefix_sum[i+1] = g_prefix_sum[i] + 1
        else:
            t_prefix_sum[i+1] = t_prefix_sum[i] + 1

    result = []

    for i in range(M):
        # calculate the difference of nucleotide sums for given sequence P[K] : Q[K]
        res_A = a_prefix_sum[Q[i]+1] - a_prefix_sum[P[i]]
        res_C = c_prefix_sum[Q[i]+1] - c_prefix_sum[P[i]]
        res_G = g_prefix_sum[Q[i]+1] - g_prefix_sum[P[i]]

        # if the sum is bigger than zero => the nucleotide occured in the sequence
        if res_A > 0:
            result.append(1)
        elif res_C > 0:
            result.append(2)
        elif res_G > 0:
            result.append(3)
        else:
            result.append(4)
    return result


s = 'CAGCCTA'
p = [2, 5, 0]
q = [4, 5, 6]

print(genomic_query_two(s, p, q))


s = 'C'
p = [0]
q = [0]
print(genomic_query_two(s, p, q))

s = 'AC'
p = [0, 0, 1]
q = [0, 1, 1]
print(genomic_query_two(s, p, q))
