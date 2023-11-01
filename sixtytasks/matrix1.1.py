import random

N = int(input("Введите кол-во строк: "))
M = int(input("Введите кол-во столбцов: "))
summa = 0

# создали матрицу
matrix = [0] * N
for i in range(N):
    matrix[i] = [0] * M

resultMatrix = [0] * (N + 1)
for i in range(N + 1):
    resultMatrix[i] = [0] * M

# заполнили матрицу и посчитали сумму всех элементов
for i in range(N):
    for j in range(M):
        matrix[i][j] = random.randint(0, 10)
        summa += matrix[i][j]


for j in range(M):
    column_sum = 0
    for i in range(N):
        column_sum += matrix[i][j]
    for i in range(N + 1):
        if i == N:
            resultMatrix[i][j] = column_sum
        else:
            resultMatrix[i][j] = matrix[i][j]



print(resultMatrix)
print(summa)
