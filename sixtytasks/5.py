#2.	Создайте словарь (город – государство).
# Найдите по введенному государству города в нем и наоборот, государство по городу. Создайте именованный кортеж, включающий государство и количество городов в нем.

from collections import namedtuple

def findKey(dictionary, value):
    countCity = 0
    Country = namedtuple("Country", "state countCity")#создали модель именованного картежа

    for key,val in dictionary.items():#поиск КЛЮЧЕЙ по значению и подсчёт кол-ва ключей
        if val == value:
            print(key)
            countCity += 1

    state = Country(value, countCity)#страна - количество городов
    print(f"\n{state}")
    print(dictionary[f"Moscow"])





dictionary = dict(Tver = "Russia", Zelenograd = "Russia", Ohio = "American", Moscow = "Russia", New_York = "American")
findKey(dictionary,"Russia")