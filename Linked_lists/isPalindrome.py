"""
Palindrome: Implement a function to check if a linked list is a palindrome.
"""

# Make a copy and reverse original linked list
# compare nodes in both linked lists
# if they are equal => Linked List is a palindrome
from node import pal1, n0, Node


def reverse_and_copy(node):
    # temp variable to hold the next node
    temp = None

    while node:
        # create new node (copy of current node)
        n = Node(node.value)
        n.next_node = temp

        # save this node into temp var
        # so you can reference it as next node
        # in next loop
        temp = n

        # move to next node to reverse the linked list
        node = node.next_node
    # after the loop
    # temp becomes the new HEAD node (was TAIL before)
    return temp


def isEqual(head1, head2):
    while head1 and head2:
        if head1.value != head2.value:
            return False

        head1 = head1.next_node
        head2 = head2.next_node
    return True


def isPalindrome(node):
    reversed_node = reverse_and_copy(node)
    return isEqual(node, reversed_node)


print(f'isPalindrome - pal1: {isPalindrome(pal1)}')
print(f'isPalindrome - n0: {isPalindrome(n0)}')
