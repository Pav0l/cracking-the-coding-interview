"""
Implementing a Stack

The stack data structure is precisely what it sounds like: a stack of data. In certain types of problems, it can
be favorable to store data in a stack rather than in an array.

A stack uses LIFO (last-in first-out) ordering. That is, as in a stack of dinner plates, the most recent item
added to the stack is the first item to be removed.
"""


class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node


class Stack:
    def __init__(self):
        self.length = 0
        self.head = None

    def add_to_stack(self, value):
        if not self.head:
            self.head = Node(value)
        else:
            # take node at head
            current_head = self.head
            # assign new node to head with default next_node = None
            self.head = Node(value)
            self.head.next_node = current_head

        self.length += 1

    def remove_from_stack(self):
        if not self.head:
            return None
        else:
            old_head_value = self.head.value
            self.head = self.head.next_node

        self.length -= 1
        return old_head_value

    def len(self):
        return self.length


s = Stack()
print(f'first len: {s.len()} ...should be 0')
s.add_to_stack(10)
print(f'added 10. HEAD = {s.head.value}. Length  {s.len()} ..should be 1')
s.add_to_stack(20)
s.add_to_stack(30)
s.add_to_stack(40)

print(f'add 20, 30, 40. HEAD = {s.head.value}. Length {s.len()} ..should be 4')

print(f'\nRemoving: {s.remove_from_stack()}')
print(f'removed 1 item: {s.len()} ..should be 3')

print(f'\nRemoving again: {s.remove_from_stack()}')
print(f'removed 1 item: {s.len()} ..should be 2')
