class Distance:
    def __init__(self,km):
        self.km=km

    def __add__(self, other):
        return self.km+ other.km

    def __sub__(self, other):
        return 

    def __mul__(self, other):
        return Distance(self.km - other.km) #creating ibject then printing 
    #we can just mul as the sub and add

    def __str__(self):
        return f"{self.km} km"




d1=Distance(10)
d2=Distance(90)

print(d1+d2)
print(d1-d2)
new_object=d1*d2
print(new_object.km)
print(d1)