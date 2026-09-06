
#caculating the sum of n natural number using the recurssioon
#parametized recusion:-basically means passing the result as parameter not using return statement 
def func(sum,initial,last_number):
    if initial>last_number:
        print(sum)
       
    else:
        
        func(sum+initial,initial+1,last_number)


func(0,1,10)

