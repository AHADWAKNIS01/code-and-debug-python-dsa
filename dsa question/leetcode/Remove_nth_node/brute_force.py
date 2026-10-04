def remove_nth(self,head,n):
    temp=head
    length=0
    while temp is not None:
        temp=temp.next
        length+=1
#first element
    if length==n:
        return head.next


    temp=head
    count=1

    lenght_nth_element=length-n
    while count<lenght_nth_element:
        temp=temp.next
        count+=1

    temp.next=temp.next.next
    return head

        


