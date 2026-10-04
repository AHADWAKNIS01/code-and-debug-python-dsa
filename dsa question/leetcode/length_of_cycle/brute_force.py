# Find Length of Cycle in Singly Linked List
#
# TC: O(n)
# SC: O(n)


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

    # Find length of cycle
    def length_of_cycle(self, head):
        temp = head
        my_dict = {}
        count = 0

        while temp is not None:

            # If node is already visited,
            # cycle is detected
            if temp in my_dict:
                return count - my_dict[temp]

            # Store node with its position
            my_dict[temp] = count

            count += 1
            temp = temp.next

        # No cycle
        return 0


# ---------------- Calling ----------------

ll = SinglyLinkedList()

ll.add(10)
ll.add(20)
ll.add(30)
ll.add(40)
ll.add(50)


# Creating cycle:
# 10 → 20 → 30 → 40 → 50
#           ↑         ↓
#           ← ← ← ← ←
ll.head.next.next.next.next.next = ll.head.next.next


# Find cycle length
result = ll.length_of_cycle(ll.head)

print("Length of cycle:", result)