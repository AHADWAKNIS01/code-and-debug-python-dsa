#counting number of frequency the number come in dictionary

num=[5,6,7,8,9,1,7,8,4,5,6,7]

freq_map={}
for i in range(0,len(num)):
    if num[i] in freq_map:
        freq_map[num[i]]=freq_map[num[i]]+1
    else:
        freq_map[num[i]]=1

#print the number frequency
x=7
print(freq_map[x])