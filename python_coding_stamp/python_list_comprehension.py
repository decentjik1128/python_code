a = [ i for i in range(10)]
print(a)
print()

b = list( i for  i in range(10))
print(b)
print()

c = [ i + 5 for i in range(10)]
print(c)
print()

d = [ i * 2 for i in range(10)]
print(d)
print()

e = [ i for i in range(10) if i % 2 == 0]
print(e)
print()

x = [i * j for i in range(2, 10) for j in range(1, 10)]
print(x)
print()

y = [[0 for j in range(2)] for i in range(3)]
print(y)
print()

z = [[0] * 2 for i in range(3)]
print(z)
print()
