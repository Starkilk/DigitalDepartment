# 2.	Создайте список, состоящий из n именованных кортежей, содержащих рейтинг книг по определённого автора. Найдите средний рейтинг от всех данных.
from collections import namedtuple


def averageValue():

    n = int(input("Введите число книг: "))
    list = [0]*n
    averageRating = 0
    Book = namedtuple("Book", "author rating")
    for i in range(n):
        author = input("Введите имя автора: ")
        rating = input("Введите рейтинг книги: ")
        tmp = Book(author, rating)
        averageRating += int(tmp.rating)
        list[i] = tmp

    averageRating //= n



    return averageRating


print(averageValue())