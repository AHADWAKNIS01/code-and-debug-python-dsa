import copy#this is use for shallow copy

original=[54,4,5,[56,78,56,32,4,3],98,100,3]
shallow=copy.deepcopy(original)

shallow[3][1]=999
shallow[6]=1000

print(original)
print(shallow)