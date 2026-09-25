#use of super ket in init
class Car:
    def __init__(self,brand:str)->None:
        self.brand=brand


class Vehicels(Car):
    def __init__(self,fuel:str,brand:str)->None:
        print("this is in init of child funtion")
        super().__init__(brand)
        self.fuel=fuel

    def display(self):
        print(f"You have a {self.brand} and the petrol type is {self.fuel}")


d1=Vehicels("petrol","maruthi")

d1.display()