#str uses
class point:
    def __init__(self,x,y):
        self.x=x
        self.y=y


    def __str__(self) -> str:
        return f"point({self.x},{self.y})"


class new:
    def __init__(self,x,y):
            self.x=x
            self.y=y



p=point(3,4)
print(p)

q=new(3,4)
print(q)