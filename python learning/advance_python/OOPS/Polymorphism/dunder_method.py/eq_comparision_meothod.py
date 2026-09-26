#eq use for comapring the object
#it cheeck the eq method is made or not
#it for for check the less than
#le for the less  then equal to check
#ge for greater then 

class Money:
    def __init__(self,amount):
        self.amount=amount
    def __eq__(self,other):
        return self.amount==other.amount

    def __it__(self,other):
        return self.amount<other.amount
    def __le__(self,other):
        return self.amount<=other.amount


a=Money(80)
b=Money(90)

print(a==b)
print(a<b)
print(a<=b)