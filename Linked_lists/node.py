"""
Create a basic Node class to use in Linked List excercises
"""


class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        # set ref to the next node in the linked list
        self.next_node = next_node


def print_nodes(node):
    while node:
        print(node.value)
        node = node.next_node


n0 = Node(10)
n1 = Node(6)
n2 = Node(5)
n3 = Node(6)
n4 = Node(7)
n5 = Node(9)
n6 = Node(14)
n7 = Node(21)

n0.next_node = n1
n1.next_node = n2
n2.next_node = n3
n3.next_node = n4
n4.next_node = n5
n5.next_node = n6
n6.next_node = n7

pal1 = Node(0)
pal2 = Node(1)
pal3 = Node(3)
pal4 = Node(1)
pal5 = Node(0)


pal1.next_node = pal2
pal2.next_node = pal3
pal3.next_node = pal4
pal4.next_node = pal5
