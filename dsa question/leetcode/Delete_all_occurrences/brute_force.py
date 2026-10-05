# Delete all occurrences of a key from Doubly Linked List
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

    # Delete all occurrences of key
    def delete_occurence_key(self, head, key):
        if head is None:
            return None

        temp = head
        new_node = head
        pre = None

        while temp is not None:
            if temp.value == key:

                if pre is not None:
                    pre.next = temp.next

                if temp.next is not None:
                    temp.next.prev = pre

                if temp == new_node:
                    new_node = new_node.next

            else:
                pre = temp

            temp = temp.next

        return new_node


# ---------------- Calling ----------------

dll = DoublyLinkedList()

dll.insert_head(10)
dll.insert_head(20)
dll.insert_head(10)
dll.insert_head(30)
dll.insert_head(10)
dll.insert_head(40)

print("Before deletion:")
dll.display()

dll.head = dll.delete_occurence_key(dll.head, 10)

print("After deletion:")
dll.display()