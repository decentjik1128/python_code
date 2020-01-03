#map
f = lambda x,y: x+y
print(f(1,4))

ex = [1, 2, 3, 4, 5]
f = lambda x: x**2
print(list(map(f,ex)))

ex = [1, 2, 3, 4, 5]
f = lambda x,y: x+y
print(list(map(f,ex,ex)))

print(list(map(lambda x: x**2 if x%2 ==0 else x,ex)))

print([value**2 for value in ex])

ex=[1, 2, 3, 4, 5]
print(list(map(lambda x: x+x, ex)))
print((map(lambda x: x+x, ex)))

f = lambda x: x**2
print(map(f,ex))
for i in map(f,ex):
    print(i)

result = map(f,ex)
print(result)
print(next(result))

import sys
print(sys.getsizeof(ex))
print(sys.getsizeof((map(lambda x: x+x, ex))))
print(sys.getsizeof(list(map(lambda x: x+x, ex))))

#reduce
from functools import reduce
print(reduce(lambda x,y: x+y, [1, 2, 3, 4, 5]))

def factorial(n):
    return reduce(lambda x,y: x*y, range(1,n+1))

print(factorial(5))
