it = [1, 2, 3].__iter__()
print(it.__next__())
print(it.__next__())
print(it.__next__())
print()
it = 'hello world!'.__iter__()
print(it.__next__())
print(it.__next__())
print(it.__next__())
print()
it = {'a' : 1, 'b' : 2, 'c' : 3}.__iter__()
print(it.__next__())
print(it.__next__())
print(it.__next__())
print()
it = {1, 2, 3}.__iter__()
print(it.__next__())
print(it.__next__())
print(it.__next__())
print()
it = range(3).__iter__()
print(it.__next__())
print(it.__next__())
print(it.__next__())