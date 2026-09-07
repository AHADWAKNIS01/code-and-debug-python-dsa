""" checking the string is palidrom  or not using loop and recusion
"""
s="mam"

n=len(s)
left=0
right=n-1
while left<right:
    if s[left]!=s[right]:
       print(False)
       break
    
    left=left+1
    right=right-1

else:
    print(True)






    