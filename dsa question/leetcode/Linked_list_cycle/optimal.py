class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    # Add node at the end
    def add(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            return

        current = self.head

        while current.next is not None:
            current = current.next

        current.next = new_node

    # Check if linked list has a cycle
    def has_cycle(self, head):
        slow = head
        fast = head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False

    # Display linked list
    def display(self):
        current = self.head

        while current is not None:
            print(current.value, end=" → ")
            current = current.next

        print("None")


# Calling

ll = SinglyLinkedList()

ll.add(10)
ll.add(20)
ll.add(30)
ll.add(40)

print(ll.has_cycle(ll.head))