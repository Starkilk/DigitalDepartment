#Подсчитать количество букв латинского алфавита в данной строке.

def latinLetters():
    string = input("Ведите строку: ")
    count = 0
    for char in string:
        if char.isalpha() and char.isascii():#проверка на то, что символ является буквой и находится в  ASCII таблице(то-есть символ латинского алфавита)
            count += 1
    return count


print(latinLetters())