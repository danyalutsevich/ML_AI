def printer(*data):
    for d in data :
        print(d, end=" ")

def printer2(**data):
    for d,val in data.items() :
        print(d,val, end=" ")

def sum(a, b):
    return a + b

printer(1,2,3,4,5,6,7,8,9,10)
print()
printer2(n1=1,n2=2)
print()
printer2(n1=1,n2=2,n3=3,n4=4,n5=5)

print(sum(b=2, a=1))

class Person:
    def __init__(self):
        self.name = "Joe Biden"
        self.age = 79
        self.children = ["Hunter", "Beau"]
        self.pets = {"Dog": "Major"}
        
    def print(self):
        print(self.name, self.age, self.children, self.pets)

joeBiden = Person()
joeBiden.print()
