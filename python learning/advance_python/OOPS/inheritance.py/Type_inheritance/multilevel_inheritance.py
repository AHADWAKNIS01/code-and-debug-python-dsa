#multiple inheritance:-tow parent one child
#grandparent->parent->child

class Flyer:
    def fly(self):
        print("flying")


class swimmer:
    def swim(self):
        print("swimming")

class duck(Flyer,swimmer):
    def quack(self):
        print("quak")


d=duck()
d.fly()
d.swim()
d.quack()
