#Matrix representation of python
matrix_a = [[3, 6], [4, 5]]#LIST
matrix_b = [(3, 6), (4, 5)]#TUPLE
matrix_c = {(0, 0) : 3, (0, 1) :6, (1,0) : 4, (1,1) : 5}#DICT

print(matrix_a, matrix_b, matrix_c)

#Maxtrix addtion
matrix_a = [[3, 6], [4, 5]]#LIST
matrix_b = [[5, 8], [6, 7]]#LIST
result = [[sum(row) for row in zip(*t)] for t in zip(matrix_a, matrix_b)]
#zip으로 묶을 시 TUPLE 형태로 묶여서 [[3,6],[5,8]] [[4,5],[6,7]] 같이 묶임
#asterisk 사용으로 [3,6] [5,8] / [4,5] [6,7]로 풀리게 됨 그리고 난 다음 zip
print(result)

#Scalar-Matrix Product
matrix_a = [[3, 6], [4, 5]]
alpha = 4
result = [[alpha * element for element in t] for t in matrix_a]
print(result)

#Matrix Transpose
matrix_a = [[1, 2, 3], [4, 5 , 6]]
result = [[ element for element in t] for t in zip(*matrix_a)]
#asterisk로 [1, 2, 3] [4, 5, 6]으로 나뉨 그 후 zip [1, 4] [2, 5], [3, 6]
print(result)

#Maxtrix Product
matrix_a = [[1, 2, 3], [4, 5, 6]]
matrix_b = [[1, 4], [2,5], [3,6]]
result = [[sum(a * b for a, b in zip (row_a, column_b)) \
            for column_b in zip(*matrix_b)] for row_a in matrix_a]
print(result)
