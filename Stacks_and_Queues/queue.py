"""
Implementing a Queue

A queue implements FIFO (first-in first-out) ordering. As in a line or queue at a ticket stand, items are
removed from the data structure in the same order that they are added.

A queue can also be implemented with a linked list. In fact, they are essentially the same thing, as long as
items are added and removed from opposite sides.
"""


class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node


class Queue:
    def __init__(self):
        self.length = 0
        self.head = None

    def add_to_queue(self, value):
        new_node = Node(value)

        if not self.head:
            self.head = new_node
        else:
            new_node.next_node = self.head
            self.head = new_node

        self.length += 1

    def remove_from_queue(self):
        if self.head == None:
            return None
        else:
            last_node = self.head
            while last_node.next_node and last_node.next_node.value != None:
                last_node = last_node.next_node

            last_node_value = last_node.value

            last_node.value = None
            last_node.next_node = None

            self.length -= 1

            return last_node_value

    def len(self):
        return self.length


q = Queue()
print(f'first len: {q.len()} ...should be 0')
q.add_to_queue(10)
print(f'added 1 item: {q.len()} ..should be 1')
q.add_to_queue(20)
q.add_to_queue(30)
q.add_to_queue(40)

print(f'add 3 more items: {q.len()} ..should be 4')


print(f'\nRemoving: {q.remove_from_queue()}')
print(f'removed 1 item: {q.len()} ..should be 3')

print(f'\nRemoving again: {q.remove_from_queue()}')
print(f'removed 1 item: {q.len()} ..should be 2')
