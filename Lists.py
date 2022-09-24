#lists
'''
1 Упорядоченные (не сортированные)
2 Динамические


'''

"""
l= [1,22,'sdf',True, 1.2]

l.pop(2)

print(l)
print(l.count(True))

cities = ["London", "Paris", "Berlin", "Madrid", "Rome", "Moscow", "New York", "Tokyo", "Beijing", "Sydney"]

cities.sort()

print(cities)
"""

n = [1,2,[10,20,30],[40,50,60],3,4,5]

n[2].insert(1,[15,16,17,18])

print(n[2][1][-2])

t = (1,2,3)
print(t)

capitals = dict(
    France="Paris",
    Germany= "Berlin",
    Italy= "Rome",
    Spain= "Madrid",
    China= "Beijing",
)

print(capitals["Germany"])

person = {}
person["Name"] = "John"
person["Age"] = 35
person["Children"] = ["Alice", "Bob"]
person["Pets"] = {"Dog": "Rex", "Cat": "Garfield"}

print(person["Pets"]["Dog"])


def fun():
    print("fun")

person["Fun"] = fun
print()

print(person.keys()) 
print(person.items()) 
print()
print(person.pop())
print()
print(person.keys()) 
print(person.items()) 