# Find Length of Cycle in Singly Linked List
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

    # Find length of cycle
    def cycle_count(self, head):
        fast = head
        slow = head

        # Detect cycle
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

            # Cycle detected
            if slow == fast:
                count = 1
                temp = slow.next

                # Count nodes in cycle
                while slow != temp:
                    count += 1
                    temp = temp.next

                return count

        # No cycle
        return 0


# ---------------- Calling ----------------

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


# Find cycle length
result = ll.cycle_count(ll.head)

print("Length of cycle:", result)