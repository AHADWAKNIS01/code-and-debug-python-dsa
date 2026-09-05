#printing number reverse using the recursion

def func(i,n):
    if i>n:
        return
    else:
        func(i+1,n)
        print(i)


func(1,30)