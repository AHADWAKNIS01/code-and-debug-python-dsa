# Doubly Linked List
#
# TC: O(1)
# SC: O(1)


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    # Insert node at the beginning
    def insert_head(self, value):
        new_node = Node(value)

        # If list is empty
        if self.head is None:
            self.head = new_node

        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node


    def display(self):
        temp = self.head

        while temp is not None:
            print(temp.value, end=" ⇄ ")
            temp = temp.next

        print("None")


    def insert_between(self,value,position):
        new_node=value
        if position==0:
            self.insert_head(value)
            return

        curr=self.head
        count=0
        while curr and count<position-1:
            curr=curr.next
            count+=1

        if curr is None:
            print("position out of bound")
            return

        new_node.next=curr.next
        new_node.pre=curr

        if curr.next:
            curr.next.prev=new_node
        curr.next=new_node

        




# Head will be:
# 30 ⇄ 20 ⇄ 10

dll = DoublyLinkedList()

dll.insert_head(10)
dll.insert_head(20)
dll.insert_head(30)

dll.display()