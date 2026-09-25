#repr uses mostly use for devloper need
#  more info as professional method
class point:
    def __init__(self,x,y):
        self.x=x
        self.y=y


    def __repr__(self) -> str:
        return f"point(x={self.x},y={self.y})"


class new:
    def __init__(self,x,y):
            self.x=x
            self.y=y



p=point(3,4)
print(p)

q=new(3,4)
print(q)