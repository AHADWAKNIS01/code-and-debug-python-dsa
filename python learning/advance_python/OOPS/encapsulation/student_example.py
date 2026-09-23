class student:
    def __init__(self,name:str,age:int,marks:list[int])->None:
        self.marks=marks

    def total(self)->int:
        return sum(self.marks)

    def average(self)->float:
        return sum(self.marks)/len(self.marks)

    def grade(self)->None:
        avg=self.average()#calling inside

        if avg>90:
            print("A")

        elif avg>50:
            print("B")

        else:
            print("c")


s1=student("anirugh",67,[89,87,67,89])
total=s1.total()
avg=s1.average()
print(f"the average is {avg} and the total is {total}")

