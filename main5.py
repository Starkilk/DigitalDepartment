from random import  randrange

#4.1 ЗАДАНИЕ №3.
# Вводится число N, необходимо отрезать от него K последних цифр. Например, при N = 123456 и K = 3 ответ должен быть 123

# N = int(input("Введите число от которого будем отрезать: "))
# K = int(input("Ввидите кол-во символов, которое хотите отрезать: "))
#
# for i in range(0, K):
#     N = N // 10
#
# print(N)

#4.2 ЗАДАНИЕ №1.
# Найти max{min(a, b), min(c, d)}

# a = int(input("Введите a: "))
# b = int(input("Введите b: "))
# c = int(input("Введите c: "))
# d = int(input("Введите d: "))
#
#
# var = {min(a, b), min(c, d)}
# answer = max(var)
# print(var)
# print(answer)

#4.3 ЗАДАНИЕ №2.
# Выведите числа от 100 до 0, при выводе все четные числа заменяйте на знак %.

# for i in range(100, -1,-1):
#     if i % 2 == 0:
#         print("%")
#     else:
#         print(i)

#4.4 ЗАДАНИЕ №2.	Сравните введенное число с загаданным случайным образом числом и выводите сообщения:
# «Число больше», «Число меньше», «Число равно», подсчитайте число попыток отгадывания числа.

# flag = True
# randNumber = randrange(1, 10)
# counter = 0
# while flag == True:
#     counter +=1
#     number = int(input("Ввидите число от 1 до 10: "))
#
#     if randNumber > number:
#         print("Число меньше")
#     if randNumber < number:
#         print("Число больше")
#     if randNumber == number:
#         print("Число равно")
#         flag = False
# print(counter)

#4.5 ЗАДАНИЕ №3.
# Создайте простой тест, включающий 3 вопроса, на которые требуется ответить, да и нет. Создайте исключение неверного ввода ответа на вопрос.

try:
    answer1 = input("Вы сегодня завтракали? Да или Нет: ")
    if (answer1 != "Да") and (answer1 != "да") and (answer1 != "нет") and (answer1 != "Нет"):
        raise ValueError("Неправильный ввод")  # определили ошибку

    answer2 = input("А обедали? Да или Нет: ")
    if answer2 != "Да" and answer2 != "да" and answer2 != "нет" and answer2 != "Нет":
        raise ValueError("Неправильный ввод")  # определили ошибку

    answer3 = input("Может ужинали? Да или Нет: ")
    if answer3 != "Да" and answer3 != "да" and answer3 != "нет" and answer3 != "Нет":
        raise ValueError("Неправильный ввод")  # определили ошибку

    print("Ну и славно :)")
except ValueError as e:
    print(f"Ошибка: {e}")





