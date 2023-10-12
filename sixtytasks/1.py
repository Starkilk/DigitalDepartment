# 1.	Заполните один кортеж десятью случайными целыми числами от 0 до 5 включительно. Также заполните второй кортеж числами от -5 до 0. Для заполнения кортежей числами напишите одну функцию. Объедините два кортежа с помощью оператора +, создав тем самым третий кортеж. С помощью метода кортежа count() определите в нем количество нулей. Выведите на экран третий кортеж и количество нулей в нем.
import random


def twoKartej():
    first = tuple([random.randint(0, 5) for _ in range(10)])
    second = tuple([random.randint(-5, 0) for _ in range(10)])
    return first, second

first, second = twoKartej()
third = first + second
countZero = third.count(0)

print(countZero)
print(third)
