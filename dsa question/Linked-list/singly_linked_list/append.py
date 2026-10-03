# Singly Linked List
# head points to the first node

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = Node(value)

        # If the list is empty
        if self.head is None:
            self.head = new_node
            return

        # Traverse to the last node
        curr = self.head

        while curr.next is not None:
            curr = curr.next

        # Connect the last node to the new node
        curr.next = new_node


# Example
ll = SinglyLinkedList()

ll.append(10)
ll.append(20)
ll.append(30)