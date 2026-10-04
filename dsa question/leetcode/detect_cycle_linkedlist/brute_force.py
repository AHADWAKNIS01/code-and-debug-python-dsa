# Singly Linked List - Detect Cycle Using Set
#
# Detects and returns the starting node of a cycle.
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

    # Detect cycle using set
    def detect_cycle(self, head):
        temp = head
        my_set = set()

        while temp is not None:

            if temp in my_set:
                return temp

            my_set.add(temp)
            temp = temp.next

        return None


# Calling

ll = SinglyLinkedList()

ll.add(10)
ll.add(20)
ll.add(30)
ll.add(40)
ll.add(50)

# Create a cycle:
# 10 → 20 → 30 → 40 → 50
#           ↑         ↓
#           ← ← ← ← ←
#
# 50 points back to 30

ll.head.next.next.next.next.next = ll.head.next.next


# Detect cycle
cycle_node = ll.detect_cycle(ll.head)

if cycle_node is not None:
    print("Cycle starts at:", cycle_node.value)
else:
    print("No cycle")