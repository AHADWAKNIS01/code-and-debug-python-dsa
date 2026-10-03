class Node:
    def __init__(self,value):
        self.value=value
        self.next=None

s1=Node(3)
s2=Node(5)
s3=Node(6)
s4=Node(7)

s1.next=s2
s2.next=s3
s3.next=s4

print(s1.value)
print(s1.next)