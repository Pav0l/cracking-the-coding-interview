"""
Stack Min: How would you design a stack which, in addition to push and pop, has a function min
which returns the minimum element? Push, pop and min should all operate in 0(1) time.
"""

# min will be another stack
# on every push, it'll check if pushed value is less than min stack value, if yes, push it to min stack as well
# on every pop, it will check if poped value is equal to current min value, if yes, it will pop it as well

from stack import Stack, Node


class minStack:
    def __init__(self):
        self.length = 0
        self.head = None
        self.min_stack = Stack()

    #  O(1) => constant push time
    def push(self, value):
        if not self.head:
            self.head = Node(value)
            self.min_stack.add_to_stack(value)
        else:
            # value is MIN
            if value < self.get_min():
                self.min_stack.add_to_stack(value)

            # take node at head
            current_head = self.head
            # assign new node to head with next_node = previous head
            self.head = Node(value)
            self.head.next_node = current_head

        self.length += 1

    #  O(1) => constant pop time
    def pop(self):
        if not self.head:
            return None
        else:
            # removed value is also MIN value
            if self.head.value == self.get_min():
                self.min_stack.remove_from_stack()

            old_head_value = self.head.value
            self.head = self.head.next_node

        self.length -= 1
        return old_head_value

    #  O(1) => constant min time
    def get_min(self):
        return self.min_stack.head.value


s = minStack()
s.push(15)
print(f'Added 15. HEAD = {s.head.value}, MIN = {s.get_min()}')
s.push(21)
print(f'Added 21. HEAD = {s.head.value}, MIN = {s.get_min()}')
s.push(13)
print(f'Added 13. HEAD = {s.head.value}, MIN = {s.get_min()}')
s.push(16)
print(f'Added 16. HEAD = {s.head.value}, MIN = {s.get_min()}')
s.push(4)
print(f'Added 4. HEAD = {s.head.value}, MIN = {s.get_min()}')
s.push(12)
print(f'Added 12. HEAD = {s.head.value}, MIN = {s.get_min()}')
a = s.pop()
print(f'Poped value: {a}. HEAD = {s.head.value}, MIN = {s.get_min()}')
a = s.pop()
print(f'Poped value: {a}. HEAD = {s.head.value}, MIN = {s.get_min()}')
a = s.pop()
print(f'Poped value: {a}. HEAD = {s.head.value}, MIN = {s.get_min()}')
a = s.pop()
print(f'Poped value: {a}. HEAD = {s.head.value}, MIN = {s.get_min()}')
