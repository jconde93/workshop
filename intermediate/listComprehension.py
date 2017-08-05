
for i in range(5):
    print(i)

'''Generators
-Slower but less memory

Comprehension
-Faster but uses more memory'''

#comprehension -notice []
xyz = [i for i in range(5)]
print(xyz)

xyz = []
for i in range(5):
    xyz.append(i)
print(xyz)

#Generator expresion -notice ()
xyz = (i for i in range(5))
print(xyz) # prints generator object
for i in xyz: # print items in generator
    print(i)
