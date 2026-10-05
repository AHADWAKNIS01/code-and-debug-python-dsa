# Reverse Doubly Linked List using Stack
#
# TC: O(n)
# SC: O(n)


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

    # Reverse doubly linked list using stack
    def reverse_doubly(self, head):
        curr=head
        prev=None
        

        if head.next is None:
            return head

        while curr is not None:
            front=curr.next

            curr.prev=front
            curr.next=prev


            
            prev =curr
            curr=front

            
        return prev

# ---------------- Calling ----------------

dll = DoublyLinkedList()

dll.insert_head(10)
dll.insert_head(20)
dll.insert_head(30)
dll.insert_head(40)

print("Before reverse:")
dll.display()

dll.head=dll.reverse_doubly(dll.head)

print("After reverse:")
dll.display()