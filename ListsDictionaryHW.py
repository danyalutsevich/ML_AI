from random import random


l1 = [1, 2, 3, 4, 5]
l2 = ['one', 'two', 'three', 'four', 'five']
d = {}

# Create a dictionary from the two lists above
if len(l1) == len(l2):
    for i in range(len(l1)):
        d[l1[i]] = l2[i]
    print(d)
else :
    print("Lists are not the same length")

d = {
        'English' : 9, 
        'Software Development' : 11, 
        'Psychology' : 8
    }

print(min(d.values()))
print(max(d.values()))

d = {
        'English' : 9, 
        'Software Development' : 11, 
        'Psychology' : 8, 
        'System Administration' : 10
    }

l = ['English', 'Psychology']

for key in l:
    if key in d:
        del d[key]
print(d)

l.clear()
for i in range(20):
    l.append(int(random()*10))
print(l)
# l.sort()


#bubble

for i in range(len(l)):
    for j in range(len(l)-1):
        if l[j] > l[j+1]:
            temp = l[j]
            l[j] = l[j+1]
            l[j+1] = temp

print(l)