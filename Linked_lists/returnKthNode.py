"""
Return Kth to Last: Implement an algorithm to find the kth to last element of a singly linked list.
"""
from node import n0

# Will utilize Runner Technique


def traverse(node, k):
    # create two pointers
    # p1 will start at node
    p1 = node
    # p2 will start at node + k nodes
    p2 = node
    for _ in range(k):
        p2 = p2.next_node
    # loop through the linked list
    # until you hit the TAIL node with p2
    # in which case, p1 will be at TAIL - k node
    # then just return the p1
    while p2:
        p2 = p2.next_node
        p1 = p1.next_node
    return p1.value


print(traverse(n0, 2))
