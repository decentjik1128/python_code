#zip
#병렬적으로 값을 추출
alist = ['a1', 'a2', 'a3']
blist = ['b1', 'b2', 'b3']
for a,b in zip(alist,blist):
    print(a,b)
#index alist[index] blist[index] 표시 
for i, (a, b) in enumerate(zip(alist, blist)):
    print(i, a, b)

#각 TUPLE은 같은 index 끼리 묶음
a,b,c = zip((1,2,3),(10,20,30),(100,200,300))
print(a,b,c)
#각 TUPLE 같은 index를 묶어 합을 list로 변환
print([sum(x) for x in zip((1,2,3), (10,20,30), (100,200,300))])
