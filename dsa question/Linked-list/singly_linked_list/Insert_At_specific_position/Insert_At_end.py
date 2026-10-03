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



    def insert_middle(self,value,position):
        new_node=Node(value)

        if position ==0:
            new_node=Node(next)
            new_node.next =self.head
            self.head=new_node

        else:
            curr=self.head
            pre=None

            count=0
            while curr is not None and count <position:
                prev_node=curr
                curr=curr.next
                count+=1

            prev_node.next=new_node
            new_node.next=curr







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



print("Before insertion:")
ll.traversal()

# Insert 15 at position 1
ll.insert_middle(15, 1)

print("\nAfter insertion:")
ll.traversal()