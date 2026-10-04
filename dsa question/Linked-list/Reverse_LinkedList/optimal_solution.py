class Node:
   
    def __init__(self,value):
            self.value=value
            self.next=None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = Node(value)

        # If the list is empty
        if self.head is None:
            self.head = new_node
            return

        # Traverse to the last node
        curr = self.head

        while curr.next is not None:
            curr = curr.next

        # Connectd the last node to the new node
        curr.next = new_node


    def Reverse_linkedlist(self,head):
        curr=head
        pre=None
        
        
        while curr is not None:
            front=curr.next
            curr.next=pre
            pre=curr
            curr=front

        

        self.head=pre
        return head

    def display(self):
        curr = self.head

        while curr is not None:
            print(curr.value, end=" → ")
            curr = curr.next

        print("None")

        

# Example
ll = SinglyLinkedList()

ll.append(10)
ll.append(20)
ll.append(30)

print("Before:")
ll.display()

ll.Reverse_linkedlist(ll.head)

print("After:")
ll.display()