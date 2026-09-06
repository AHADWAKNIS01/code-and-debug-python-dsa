
#caculating the sum of n natural number using the recurssioon

def func(sum,initial,last_number):
    if initial>last_number:
        print(sum)
        return
    else:
        sum+=initial
        func(sum,initial+1,last_number)


func(0,1,10)

