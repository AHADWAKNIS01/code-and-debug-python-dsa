num=[1,2,34,5,65,7,7,88,9,]


def func(num,left,right):
    if left>=right:
        return
    else:
        num[left], num[right]=num[right], num[left]
        func(num,left+1,right-1)

func(num,0,len(num)-1)
print(num)


