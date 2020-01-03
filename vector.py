#Vector representation of python
vector_a = [1, 2, 10]#LIST
vector_b = (1, 2, 10)#TUPLE
vector_c = {'x' : 1, 'y' : 1, 'z' : 10}#DICT
print(vector_a, vector_b, vector_c)

#Vector의 계산
u = [2, 2]
v = [2, 3]
z = [3, 5]
result = [sum(t) for t in zip(u, v, z)]
print(result)

u = [1, 2, 3]
v = [4, 4, 4]
alpha = 2
result = [alpha * sum(t) for t in zip(u, v)]
print(result)

#Scalar-Vector product
u = [1, 2, 3]
v = [4, 5, 6]
a = 5
print([5 * sum(z) for z in zip(u, v)])
