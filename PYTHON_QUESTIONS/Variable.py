class A :
    def __init__(self):
        self.i=1
        self.j=5
    def display(self):
        print(self.i,self.j)

class B(A):
    def __init__(self):
        super().__init__()
        self.i=2
        self.j=7

c=B()
c.display()


def fruits():
    yield "Mango"
    yield "Jackfruit"
    yield "Banana"
    yield "Gauva"

getFruits=fruits()
for a in getFruits:
    print(a)