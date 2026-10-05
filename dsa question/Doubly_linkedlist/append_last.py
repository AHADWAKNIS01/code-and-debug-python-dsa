
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self,value):
        new_node=Node(value)
        if not self.head:
            self.head=new_node
        else:
            current=self.head
            while current.next:
                current=current.next

            current.next=new_node
            new_node.prev=current

