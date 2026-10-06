# Remove duplicates from a Sorted Doubly Linked List
#
# TC: O(n)
# SC: O(1)



class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    # Insert at head
    def insert_head(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            return

        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node

    # Display list
    def display(self):
        temp = self.head

        while temp is not None:
            print(temp.value, end=" ⇄ ")
            temp = temp.next

        print("None")

    # Remove duplicates
    def remove_duplicate(self, head):
        curr = head

        while curr is not None and curr.next is not None:
            if curr.value == curr.next.value:
                duplicate = curr.next
                curr.next = duplicate.next

                if curr.next is not None:
                    curr.next.prev = curr
            else:
                curr = curr.next

        return head


# ---------------- Calling ----------------

dll = DoublyLinkedList()

dll.insert_head(40)
dll.insert_head(30)
dll.insert_head(30)
dll.insert_head(20)
dll.insert_head(20)
dll.insert_head(20)
dll.insert_head(10)

print("Before removing duplicates:")
dll.display()

dll.head = dll.remove_duplicate(dll.head)

print("After removing duplicates:")
dll.display()