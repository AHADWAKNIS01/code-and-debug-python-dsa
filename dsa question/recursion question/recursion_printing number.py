n=30#ending number
#i starting number
def func(i,n):
    if i>n:
        return
    else:
        print(i)
        func(i+1,n)

func(1,30)

    
