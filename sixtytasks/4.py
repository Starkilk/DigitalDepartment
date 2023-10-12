#1.	Создайте словарь, где ключами являются числа, а значениями – строки. Примените к нему метод items(),
# полученный объект dict_items передайте в написанную вами функцию, которая создает и возвращает новый словарь, "обратный" исходному, т. е.
# ключами являются строки, а значениями – числа.

def reverser(dict_items):

    reversed_digits = dict((value, key) for key, value in dict_items)
    print(reversed_digits)



digits = {1 : "один", 2:"два", 3:"три", 4:"четыре", 5:"пять"}
dict_items = digits.items()

reverser(dict_items)