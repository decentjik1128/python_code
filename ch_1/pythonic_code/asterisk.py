#asterisk
def asterisk_test0(a,*args):
    print(a,args)
    print(type(args))
asterisk_test0(1,2,3,4,5,6)

def asterisk_test1(a,**kargs):
    print(a,kargs)
    print(type(kargs))
asterisk_test1(1,b=2,c=3,d=4,e=5,f=6)

def asterisk_test2(a,*args):
    print(a,args[0])
    print(type(args))
asterisk_test2(1,(2,3,4,5,6))

def asterisk_test3(a,*args):
    print(a,*args)
    print(type(args))
asterisk_test3(1,*(2,3,4,5,6))

a, b, c = ([1,2], [3,4], [5,6])
print(a,b,c)

data = ([1.2], [3.4], [5,6])
print(*data)
print(data)

for data in zip(*([1,2], [3,4], [5,6])):
    print(sum(data))

def asterisk_test4(a,b,c,d,e=0):
    print(a,b,c,d,e)

data = {"d":1, "c":2, "b":3, "e":56}
asterisk_test4(10,**data)
