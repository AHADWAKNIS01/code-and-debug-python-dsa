""" checking the string is palidrom  or not using loop and recusion
"""

#using for loop
# s="mam"

# n=len(s)
# left=0
# right=n-1
# while left<right:
#     if s[left]!=s[right]:
#        print(False)
#        break
    
#     left=left+1
#     right=right-1

# else:
#     print(True)

#using recursion


def func(s,left,right):
    if left>=right:
        return True
    
    if s[left]!=s[right]:
        return False

    return func(s,left+1,right-1)



print(func("jhj",0,len("jhj")-1))




    