"""
Remove Dups: Write code to remove duplicates from an unsorted linked list.
"""
from node import n0


def print_nodes(node):
    while node:
        print(node.value)
        node = node.next_node


print(f'Linked list:')
print_nodes(n0)


def remove_dup(node):
    unique = set()
    previous = node

    while node:
        if node.value in unique:
            previous.next_node = node.next_node
        else:
            unique.add(node.value)
            previous = node
        node = node.next_node


remove_dup(n0)

print(f'LL after removing dups:')
print_nodes(n0)
