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


s = 'CAGCCTA'
p = [2, 5, 0]
q = [4, 5, 6]

print(genomic_query(s, p, q))
