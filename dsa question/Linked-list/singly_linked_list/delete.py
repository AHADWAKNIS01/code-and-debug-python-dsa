
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




        # Insert at end
    def insert_end(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            return

        curr = self.head

        while curr.next is not None:
            curr = curr.next

        curr.next = new_node


        # Delete a node by value
    def delete(self, value):
        curr = self.head

        # Case 1: List is empty
        if curr is None:
            print("The list is empty")
            return

        # Case 2: Delete the first node
        if curr.value == value:
            self.head = curr.next
            return

        # Case 3: Delete a node from middle/end
        prev = None

        while curr is not None:
            if curr.value == value:
                prev.next = curr.next
                return

            prev = curr
            curr = curr.next

        # Case 4: Value not found
        print("The node not found")






# Example
ll = SinglyLinkedList()

ll.append(10)
ll.append(20)
ll.append(30)





print("Before insertion:")
ll.traversal()

# Insert 15 at position 1
ll.insert_middle(15, 1)

print("\nAfter insertion:")
ll.traversal()

ll.insert_end(40)

print("\nAfter insertion at end:")
ll.traversal()


print("\nBefore deletion:")
ll.traversal()

# Delete node with value 20
ll.delete(20)

print("\nAfter deleting 20:")
ll.traversal()

# Delete first node
ll.delete(10)

print("\nAfter deleting 10:")
ll.traversal()

# Try deleting a value that doesn't exist
ll.delete(100)