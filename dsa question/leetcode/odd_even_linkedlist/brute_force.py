def odd_even(self,head):
    temp=head
    value=[]
    if head is None or head.next is None:
        return head

    #odd indices
    while temp is not None:
        value.append(temp.val)
        if temp.next is None:
            break
        temp = temp.next.next



#event indeces
    temp=head.next
    while temp is not None:
        value.append(temp.val)
        if temp.next is None:
                    break
        temp = temp.next.next

    temp=head
    index=0
    while temp is not None:
        temp.val=value[index]
        index+=1
        temp=temp.next

    return head

