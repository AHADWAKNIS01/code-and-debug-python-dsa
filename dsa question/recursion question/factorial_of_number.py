""" factorial number:-base condition will be n==1 then print 1
or else print n*n-1


"""

def func(n):
    if n==1:
        return 1
    else:
        return n*func(n-1)

print(func(9))


