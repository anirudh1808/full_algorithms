class Dog :
    tricks=[]
    def __init__(self,name):
        self.name=name
    def add_tricks(self,trick):
        self.tricks.append(trick)
d=Dog('Fido')
e=Dog('Buddy')
d.add_tricks('roll')
e.add_tricks('play')
print(d.tricks)
