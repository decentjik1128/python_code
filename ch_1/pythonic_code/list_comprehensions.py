#List Comprehension
result = [i for i in range(10)]
print(result)

#조건을 만족할 때만 추가
result = [i for i in range(10) if i%2 == 0]
print(result)

#이중 for문 방식
word_1 = 'Hello'
word_2 = 'World'
#1차원 방
result = [i+j for i in word_1 for j in word_2]
print(result)

case_1 = ['A', 'B', 'C']
case_2 = ['D', 'E', 'A']
#1차원 방식
result = [i+j for i in case_1 for j in case_2]
print(result)
#2차원 방식
result = [[i+j for i in case_1] for j in case_2]
print(result)
#1차원 방식 + 필터 추가
result = [i+j for i in case_1 for j in case_2 if not(i==j)]
print(result)
result.sort()
print(result)

words = 'The quick brown fox jumps over the lazy dogl'.split()
print(words)

stuff=[[w.upper() , w.lower(), len(w)]for w in words]
for i in stuff:
    print(i)
