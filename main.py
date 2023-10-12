number = int(input("Введите 3ёх значное число: "))
flag = True #флаг, чтобы зациклить введение числа после некорректного ввода

while flag == True:
    if 100 <= number <= 999:
        flag = False

        #разбило число на 3 цифры
        digit1 = number//100
        digit2 = number//10 % 10
        digit3 = number % 10

        #получили все комбинации
        rearrangement1 = str(digit1) + str(digit2) + str(digit3)
        rearrangement2 = str(digit1) + str(digit3) + str(digit2)
        rearrangement3 = str(digit2) + str(digit1) + str(digit3)
        rearrangement4 = str(digit2) + str(digit3) + str(digit1)
        rearrangement5 = str(digit3) + str(digit1) + str(digit2)
        rearrangement6 = str(digit3) + str(digit2) + str(digit1)

        #вывели результат
        print("Результат: \n")
        print(rearrangement1)
        print(rearrangement2)
        print(rearrangement3)
        print(rearrangement4)
        print(rearrangement5)
        print(rearrangement6)

    else:
        #некорректное число
        print("Число введено некорректно, попробуйте ещё раз.")
        number = int(input("Введите 3ёх значное число: "))
