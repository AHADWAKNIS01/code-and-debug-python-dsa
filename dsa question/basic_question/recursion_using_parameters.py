#basic printing number i n time
x=15#number
n=3#number of time to print
def func(x,n):
    if n==0:
        return
    else:
        print(x)
        func(x,n-1)

func(x,n)