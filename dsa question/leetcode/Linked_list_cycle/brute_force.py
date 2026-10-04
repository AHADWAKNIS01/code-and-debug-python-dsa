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

    # Detect cycle using set
    def cycle_linkedlist(self, head):
        temp = head
        my_set = set()

        while temp is not None:

            # If node already exists in set, cycle exists
            if temp in my_set:
                return True

            my_set.add(temp)
            temp = temp.next

        return False


# Calling

ll = SinglyLinkedList()

ll.add(10)
ll.add(20)
ll.add(30)
ll.add(40)

print(ll.cycle_linkedlist(ll.head))