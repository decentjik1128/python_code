#enumerate
#list의 있는 index와 값을 unpacking
for i,v in enumerate(['tic', 'tac', 'toe']):
    print(i,v)

#list에 있는 index와 값을 unpacking 하여 list로 저
mylist = ['a', 'b', 'c', 'd']
print(list(enumerate(mylist)))
#문장을 list로 만들고 list의 index와 값을 unpacking하여 list로 저장
print({i:j for i,j in enumerate('Gachon University is an academic institute located in South Korea.'.split())})
