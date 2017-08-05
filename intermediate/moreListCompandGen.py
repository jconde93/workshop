
input_list = [5,6,2,20,15,4,8]

def div_by_five(num):
    if num % 5 == 0:
        return True
    else:
        return False

# Generator
xyz = (i for i in input_list if div_by_five(i))

# for i in xyz:
#     print(i)

# [print(i) for i in xyz]

# Comprehension
xyz2 = [i for i in input_list if div_by_five(i)]
# print(xyz)

[[print(x,y) for y in range(5)] for x in range(5)]