a = [10, 20, 30]
print(*a)

def print_numbers(*args):
    for arg in args:
        print(arg, end = ' ')
    print()

print_numbers(10, 20, 30)
print_numbers(*[10, 20, 30, 40, 50])
print()

def personal_info(name, age, address):
    print('name : ', name)
    print('age : ', age)
    print('address : ', address)

x={'name' : 'jung', 'age' : 30, 'address' : 'seoul youngsan'} #함수의 매개변수의 이름과 딕셔너리의 키 이름이 같아야함
personal_info(**x)
# *x하면은 키 값을 사용하겠다는 의미

def personal_info2(**kwargs):
    for kw, arg in kwargs.items():
        print(kw, ':', arg, sep = '')

personal_info2(**x)
