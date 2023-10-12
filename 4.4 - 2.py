#4.4 ЗАДАНИЕ №2.	Сравните введенное число с загаданным случайным образом числом и выводите сообщения:
# «Число больше», «Число меньше», «Число равно», подсчитайте число попыток отгадывания числа.
from random import randrange

flag = True
randNumber = randrange(1, 10)
counter = 0
while flag == True:
    counter +=1
    number = int(input("Ввидите число от 1 до 10: "))

    if randNumber > number:
        print("Число меньше")
    if randNumber < number:
        print("Число больше")
    if randNumber == number:
        print("Число равно")
        flag = False
print(counter)