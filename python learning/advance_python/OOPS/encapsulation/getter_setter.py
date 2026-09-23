class bank:
    def __init__(self,name):
        self.__name: str=name
        

    def setter(self,name):
            self.__name=name


    def getter(self):
        return self.__name

  



s1=bank("ahad",)
print(s1.getter())
s1.setter("waknis")
print(s1.getter())
