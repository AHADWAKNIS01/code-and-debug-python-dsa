# Singly Linked List - Traversal and Insert at Beginning
#
# Traversal means visiting each node one by one,
# starting from the head.
#
# Example:
# head
#  ↓
# [10] → [20] → [30] → None


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    # Insert at the end
    def append(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            return

        curr = self.head

        while curr.next is not None:
            curr = curr.next

        curr.next = new_node

    # Traversal
    def traversal(self):
        curr = self.head

        while curr is not None:
            print(curr.value, end=" ")
            curr = curr.next

    # Insert at beginning
    def insert_beginning(self, value):
        new_node = Node(value)

        # New node points to current head
        new_node.next = self.head

        # New node becomes the new head
        self.head = new_node


   

# Example
ll = SinglyLinkedList()

ll.append(10)
ll.append(20)
ll.append(30)

print("Before insertion:")
ll.traversal()

ll.insert_beginning(5)

print("\nAfter insertion:")
ll.traversal()