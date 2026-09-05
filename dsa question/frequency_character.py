#character frequency is counting with constriant is given
#a<s<z
#a start from 97

s="azxcbkdhakfhiuyeo"
q=["d","a","y","x"]

hash_list=[0]*26

for ch in s:
    ascci_value=ord(ch)
    index =ascci_value-97 #for a=0 index we will get
    hash_list[index]+= 1
    
#as per index
print("printing as per character given")
print("=================================")
for ch in q:
    ascci_value=ord(ch)
    index =ascci_value - 97

    print(hash_list[index])

print("=================================")

print("print all charcter wise ")
for i in range(26):
    print(i,chr(i+97),hash_list[i])

