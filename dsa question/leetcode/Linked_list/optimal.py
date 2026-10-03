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

    # Find middle element
    def middle_element(self, head):
        slow = head
        fast = head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        return slow


# Calling
ll = SinglyLinkedList()

ll.append(10)
ll.append(20)
ll.append(30)
ll.append(40)
ll.append(50)

middle = ll.middle_element(ll.head)

print("Middle element:", middle.value)