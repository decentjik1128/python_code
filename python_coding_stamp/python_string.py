a = 'Hello, world!'
b = a.replace('world', 'Python')

print(a)
print(b)

table = str.maketrans('aeiou', '12345')
'apple'.translate(table)

c = a.split()
print(c)

d = '-'.join(c)
print(d)

e = 'python'.ljust(10)
print(e, len(e))

f = 'python'.rjust(10)
print(f, len(f))

g = 'python'.center(10)
print(g, len(g))

h = 'python'.zfill(10)
print(h)

i = 'Hello, {0} {2} {1}'.format('Python', 'Script', 3.6)
print(i)

j = f'Hello, {a} {b}'
print(j)
