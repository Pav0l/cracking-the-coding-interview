"""
Given two strings, determine if they share a common substring.
A substring may be as small as one character.

For example, the words "a", "and", "art" share the common substring.
The words "be" and "cat" do not share a substring.

The function should return a string, either "YES" or "NO" based on whether
the strings share a common substring.
"""


def two_strings(s1, s2):
    one = set(s1)

    for i in s2:
        if i in one:
            return 'YES'
    return 'NO'


print(two_strings('onee', 'wta'))
