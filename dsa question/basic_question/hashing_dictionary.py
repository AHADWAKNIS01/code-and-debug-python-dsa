#if constraint is not given then use the dictionary
num=[1,2,3,4,5,6,7,8,9,5,10]#element

index=[10,11,111,15,17,16,2,3]#index


dict={}

for i in range(0,len(num)):
    if num[i] in dict:
        dict[num[i]]=dict[num[i]] +1
    else:
        dict[num[i]]=1

result={}
for i in range(0,len(index)):
    if index[i] in dict:
        result[index[i]]=dict[index[i]]

    else:
        result[index[i]]=0

print(result)



   
    

