def add_number(x):
    x=x+1
    print(f"the value of x inside the block is ={x}")



num=10#this is an immutable object
add_number(num)
print(f"Outside function={num}")