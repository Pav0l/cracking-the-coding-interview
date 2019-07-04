"""
Is Unique: Implement an algorithm to determine if a string has all unique characters.
What if you cannot use additional data structures?
"""


def isUnique(word):
    # Time complexity: O(n)
    # Space complexity: O(n)
    return len(set(word)) == len(word)
# Another solution would use for loop in the word string
# add the character to a dictionary with key value being the letter of word
# and checking in every loop move, if that character already exists in the dict
# if not, return True, else return False


def isUniqueTwo(word):
    # brute force solution without using any aditional data structures
    # Time complexity: O(n^2)
    # Space complexity: O(1)
    for i in range(len(word)):
        for j in range(i+1, len(word)):
            if word[i] == word[j]:
                return False
    return True


print(isUnique('mom'))
print(isUniqueTwo('mom'))
