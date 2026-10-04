# Singly Linked List - Detect Cycle
#
# Detects the starting node of a cycle
# using Floyd's Cycle Detection Algorithm.
#
# TC: O(n)
# SC: O(1)


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

    # Detect cycle and return starting node
    def detect_cycle(self, head):

        slow = head
        fast = head

        # Phase 1: Detect cycle
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:

                # Phase 2: Find cycle starting point
                slow = head

                while slow != fast:
                    slow = slow.next
                    fast = fast.next

                return slow

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
ll.head.next.next.next.next.next = ll.head.next.next


# Detect cycle
cycle_node = ll.detect_cycle(ll.head)

if cycle_node is not None:
    print("Cycle starts at:", cycle_node.value)
else:
    print("No cycle")