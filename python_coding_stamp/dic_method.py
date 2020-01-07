x = {'a' : 10, 'b' : 20, 'c' : 30, 'd' : 40}

x.setdefault('e')
print(x)

x.setdefault('f', 100)
print(x)

x.update(a = 90)
print(x)

x.update(g = 0)
print(x)
