w=5
def f(x):
    w=2
    def g(y):
        w=4
        def h(z):
            global  w
            return w*x+y+z

        return h
    return g

print(f(5)(5)(5))

def foo():
    try:
        return 5
    except :
        return 6
    finally:
        return 8
print(foo())


def func1(x,y):
    print(x/y)

def func2(x, y):
    print(x // y)
func1(5,2)
func1(5.0,2)
func2(5,2)
func1(5.0,2)


l1=[1,2,3]
l2=[4,5,6]

l4=[]
for x in l1:
    for y in l2:
        l4.append(x*y)
print(l4)
l3=[x*y for x,y in zip(l1,l2)]
print(l3)

l5=[map((lambda x,y:x*y),l1,l2)]
print(l5)

l6=[x*y for x in l1 for y in l2]
print(l6)