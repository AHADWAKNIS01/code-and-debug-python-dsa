#functional recursion:-1)create the flow
       #               2)create the based the condition
#basically means returning the resulth from the result return n + func(n-1)

def func(n):
    if n==1:
        return 1
    else:
        return n+func(n-1)

print(func(10))