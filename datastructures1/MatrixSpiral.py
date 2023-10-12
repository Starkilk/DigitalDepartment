
def sumMainDiagonal():

    sumDiagonal = 0#сумма чисел главной диагонали
    orderMatrix = int(input("Введите порядк матрицы:"))
    digit = 1#переменная для заполнения матрицы
    #границы матрицы
    left = 0
    right = orderMatrix - 1
    top = 0
    bottom = orderMatrix - 1

    #создали матрицу
    matrix = [0]*orderMatrix
    for i in range(orderMatrix):
        matrix[i] = [0] * orderMatrix

    #заполнили матрицу
    while digit <= orderMatrix * orderMatrix:
        # Заполняем верхнюю границу слева направо
        for i in range(left, right + 1):
            matrix[top][i] = digit
            digit += 1
        top += 1

        # Заполняем правую границу сверху вниз
        for i in range(top, bottom + 1):
            matrix[i][right] = digit
            digit += 1
        right -= 1

        # Заполняем нижнюю границу справа налево
        for i in range(right, left - 1, -1):
            matrix[bottom][i] = digit
            digit += 1
        bottom -= 1

        # Заполняем левую границу снизу вверх
        for i in range(bottom, top - 1, -1):
            matrix[i][left] = digit
            digit += 1
        left += 1

    print(matrix)

    #посчитали сумму чисел главной диагонали
    for i in range(orderMatrix):
            sumDiagonal += matrix[i][i]


    return sumDiagonal



print(sumMainDiagonal())


