fruits = {'apple', 'strawberry', 'grape', 'orange', 'pineapple', 'cherry', 'strawberry', 'grape', 'orange'}
print(fruits)
print(type(fruits))

a = set('apple')
print(a)

b = set(range(5))
print(b)

c = set()
print(c)
print(type(c))

d = {}
print(d)
print(type(d))

print(a|b)
print(set.union(a, b))
print(a.update(b))

print(a&b)
print(set.intersection(a, b))

print(a-b)
print(set.difference(a, b))

print(a^b)
print(set.symmetric_difference(a, b))

a = {1, 2, 3, 4}

print(a <= {1, 2, 3, 4})
print(a.issubset({1, 2, 3, 4, 5}))
print(a.isdisjoint({5, 6, 7, 8}))
print(a.isdisjoint({3, 4, 7, 8}))
print()

a.add(5)
print(a)
a.remove(5)
print(a)
a.discard(4)
print(a)
a.discard(7)
print(a)
print(a.pop())
print(a)
a.clear()
print(a)

a = {i for i in 'apple'}
print(a)
a = {i for i in 'pineapple' if i not in 'apl'}
print(a)
