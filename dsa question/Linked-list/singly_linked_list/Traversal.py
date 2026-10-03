# Singly Linked List - Traversal
#
# Traversal means visiting each node of the linked list
# one by one, starting from the head.
#
# Example:
# head
#  ↓
# [10] → [20] → [30] → None
#
# Output:
# 10 20 30


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            return

        curr = self.head

        while curr.next is not None:
            curr = curr.next

        curr.next = new_node

    def traversal(self):
        # Start from the first node
        curr = self.head

        # Visit every node until the end
        while curr is not None:
            print(curr.value, end=" ")

            # Move to the next node
            curr = curr.next


# Example
ll = SinglyLinkedList()

ll.append(10)
ll.append(20)
ll.append(30)

ll.traversal()