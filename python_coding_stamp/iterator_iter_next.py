it = iter(range(3))
print(next(it))
print(next(it))
print(next(it))

import random
it = iter(lambda : random.randint(0,5), 2)
print(next(it))
print(next(it))

for i in iter(lambda : random.randint(0, 5), 2):
    print(i, end = ' ')

while True:
    i = random.randint(0,5)
    if i ==2:
        break;
    print(i, end = ' ')

it = iter(range(3))
print(next(it,10))
print(next(it,10))
print(next(it,10))
print(next(it,10))
