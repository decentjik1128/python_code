file = open('hello.txt', 'w')
file.write('Hello, world!')
file.close()

file = open('hello.txt', 'r')
print(file.read())
file.close()

with open('hello.txt', 'r') as file:
    s = file.read()
    print(s)

with open('hello.txt', 'w') as file:#개행 문자 지정해 주어야지 개행이 진행됨!!
    for i in range(3):
        file.write('Hello, world! {0}\n'.format(i))

lines = ['Hello.\n', 'Python\n', 'coding stamp.\n']

with open('hello txt', 'w') as file:
    file.writelines(lines)

with open('hello txt', 'r') as file:
    lines = file.readlines()
    print(lines)

with open('hello txt', 'r') as file:
    line = None
    while line != '':
        line = file.readline()
        print(line.strip('\n'))

import pickle

name = 'james'
age = 17
address = 'seoul seocho banfo'
scores = {'korean' : 90, 'english' : 95, 'mathematics' : 85, 'science' : 82}

with open('james.p', 'wb') as file:
    pickle.dump(name, file)
    pickle.dump(age, file)
    pickle.dump(address, file)
    pickle.dump(scores, file)

with open('james.p', 'rb') as file:
    name = pickle.load(file)
    age = pickle.load(file)
    address = pickle.load(file)
    scores = pickle.load(file)
    print(name)
    print(age)
    print(address)
    print(scores)
