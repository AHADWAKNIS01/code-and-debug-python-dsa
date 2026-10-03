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
        curr = self.head

        while curr is not None:
            print(curr.value, end=" ")
            curr = curr.next

    # Delete a node by value
    def delete(self, value):
        curr = self.head

        # Empty list
        if curr is None:
            print("The list is empty")
            return

        # Delete first node
        if curr.value == value:
            self.head = curr.next
            return

        # Delete middle/end node
        prev = None

        while curr is not None:
            if curr.value == value:
                prev.next = curr.next
                return

            prev = curr
            curr = curr.next

        print("The node not found")