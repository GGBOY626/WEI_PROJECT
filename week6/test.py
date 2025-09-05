# extract information with age greater than 25 from the following list of dictionaries
data = [{"name": "Alice", "age": 28}, {"name": "Bob", "age": 24}, {"name": "Charlie", "age": 30}]

result =[]
for i in data:
    if i['age']>25:
        result.append(i)
print(result)

# use list comprehension to flatten the matrix
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

result2 = []
for i in matrix:
    for j in i:
        result2.append(j)
print(result2)

matrix2 = [[0, 2, -3], [4, -5, 16], [17, 18, 39]]

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        matrix[i][j] += matrix2[i][j]

print(matrix)


matrix3 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

matrix4 = [[0, 2, -3], [4, -5, 16], [17, 18, 39]]

for i in range(len(matrix3)):
    for j in range(len(matrix3[i])):
        matrix3[i][j] *= matrix4[i][j]

print(matrix3)