"""
Create a basic Node class to use in Linked List excercises
"""


class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        # set ref to the next node in the linked list
        self.next_node = next_node
