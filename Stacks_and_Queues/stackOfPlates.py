"""
Stack of Plates:
Imagine a (literal) stack of plates. If the stack gets too high, it might topple.
Therefore, in real life, we would likely start a new stack when the previous stack exceeds some
threshold.

Implement a data structure SetOfStacks that mimics this. SetOfStacks should be
composed of several stacks and should create a new stack once the previous one exceeds capacity.
SetOfStacks. push () and SetOfStacks. pop() should behave identically to a single stack
(that is, pop ( ) should return the same values as it would if there were just a single stack).

FOLLOW UP
Implement a function popAt (int index) which performs a pop operation on a specific substack.
"""

# IDEA 1:
# SetOfStacks will keep track of substacks in a dict
# SetOfStacks will keep track of number of substacks
# dict key will be number of substack
# push and pop will always work on the last substack
# popAt will perform pop from dict[key] stack

# IDEA 2:
# Stack inside a stack
# SetOfStacks will be a Stack
# Every node in SetOfStacks will be a head node of substack
# head node of SetOfStacks is a head node of the last substack (the one which you'll use for push/pop)
# popAt will have to loop through SetOfStack nodes to find head at index

# IDEA 1 is more time efficient, as it does all operations at O(1) constant time
# IDEA 2 does popAt at O(n) linear time based on number of substacks

# To clarify: If you popAt specific substack, should you then push into that empty substack?

from stack import Stack, Node


# idea 1 implementation
class SetOfStacks:
    def __init__(self, stack_capacity):
        self.stack_capacity = stack_capacity
        self.stacks = {}

    def set_of_stacks_len(self):
        return len(self.stacks)

    def get_push_key(self):
        # first stack key == 1
        if self.set_of_stacks_len() == 0:
            return 1
        else:
            head_stack = self.stacks[self.set_of_stacks_len()]
            # if the stack has reached capacity, return key for next stack
            if head_stack.length == self.stack_capacity:
                return self.set_of_stacks_len() + 1
            else:
                return self.set_of_stacks_len()

    def push(self, value):
        # get stack key
        # either current stack which has not reached capacity yet
        # or new stack ket
        key = self.get_push_key()

        # for new stack, create the key:value pair first
        if key not in self.stacks:
            self.stacks[key] = Stack()

        st = self.stacks[key]
        st.add_to_stack(value)

    def pop(self):
        # get last stack key => length of stacks dict
        key = self.set_of_stacks_len()
        st = self.stacks[key]
        removed_value = st.remove_from_stack()

        # if you removed the last item from substack
        # pop the key from dict
        if st.length == 0:
            self.stacks.pop(key)

        return removed_value

    def popAt(self, key):
        if key not in self.stacks:
            print('ERROR: Stack key/index does not exist in Set of Stacks')
            return None

        st = self.stacks[key]
        removed_value = st.remove_from_stack()

        return removed_value


a = SetOfStacks(3)
print(f'SetOfStack len: {a.set_of_stacks_len()}. Should be 0')
a.push(1)
a.push(2)
a.push(3)
a.push(4)
print(f'SetOfStack len: {a.set_of_stacks_len()}. Should be 2')
a.push(5)
a.push(6)
a.push(7)
a.push(8)
print(f'SetOfStack len: {a.set_of_stacks_len()}. Should be 3')
print(f'Pop: {a.pop()}')
print(f'SetOfStack len: {a.set_of_stacks_len()}. Should be 3')
print(f'Pop: {a.pop()}')
print(f'SetOfStack len: {a.set_of_stacks_len()}. Should be 2')
a.push(9)
print(f'SetOfStack len: {a.set_of_stacks_len()}. Should be 3')
print(f'Pop at stack 1. Value: {a.popAt(1)}')
