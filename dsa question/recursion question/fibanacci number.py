""" finding fibanacci number 
0 1  1 2 3 5 8 13 21 34 
"""

def func(num):
    if num==0 or num==1:
        return num

    return func(num-1)+func(num-2)


print(func(6))#5th fibanacci number





