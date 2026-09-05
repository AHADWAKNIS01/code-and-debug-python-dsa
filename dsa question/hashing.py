n=[1,2,3,4,5,6,7,8,9,5,10]#element

m=[10,11,111,15,17,16,2,3]#index

#making hash array of size 11
hash_list=[0]*11
for num in n:
    hash_list[num]=hash_list[num]+1

for num in m:
    if num<1 or num>10:
        print(0)
    else:
        print(hash_list[num])



