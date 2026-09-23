class Student:
    roll_no=0
    name=""
    age=0

    def set_details(self,r,a):
        self.roll_no=r
        self.age=a

    def display_detials(self):
        print(self.roll_no)
        print(self.age)


#object or instance created as s1
s1=Student()
s1.set_details(56,42)
s1.display_detials()
s2=Student()

s2.set_details(23,78)
s2.display_detials()

