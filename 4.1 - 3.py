#4.1 ЗАДАНИЕ №3.
# Вводится число N, необходимо отрезать от него K последних цифр. Например, при N = 123456 и K = 3 ответ должен быть 123

N = int(input("Введите число от которого будем отрезать: "))
K = int(input("Ввидите кол-во символов, которое хотите отрезать: "))

for i in range(0, K):
    N = N // 10

print(N)