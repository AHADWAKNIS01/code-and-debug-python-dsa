class bank:
    def __init__(self,name,balance):
        self.name: str=name
        self.__balance=balance

    def deposit(self,amount:int):
        if amount <0:
            print("invalid amout")
        else:
            self.__balance+=amount

    def display_balance(self):
        return self.__balance



s1=bank("ahad",500)
print(s1.display_balance())
s1.deposit(5000)
print(s1.display_balance())
print(s1._bank__balance) #access the private virable