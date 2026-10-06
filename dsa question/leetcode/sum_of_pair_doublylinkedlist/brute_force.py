# Find all pairs with given sum in Doubly Linked List
#
# TC: O(n^2)
# SC: O(k)
# k = number of pairs found


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

    # Find pairs with given sum
    def sum_of_pair(self, head, target):
        temp = head
        resulth = []

        while temp is not None:
            temp1 = temp.next

            while temp1 is not None:
                if temp.value + temp1.value == target:
                    resulth.append((temp.value, temp1.value))

                temp1 = temp1.next

            temp = temp.next

        return resulth


# ---------------- Calling ----------------

dll = DoublyLinkedList()

dll.insert_head(10)
dll.insert_head(20)
dll.insert_head(30)
dll.insert_head(40)
dll.insert_head(50)

print("Doubly Linked List:")
dll.display()

target = 60

result = dll.sum_of_pair(dll.head, target)

print("Pairs with sum", target, ":", result)