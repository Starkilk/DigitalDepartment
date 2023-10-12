#2.	Вводится строка, включающая строчные и прописные буквы.
# Требуется вывести ту же строку, заменив в ней строчные буквы прописными, а прописные – строчными.
# Например, исходная строка – "aB!cDEf", новая строка – "Ab!CdeF".
# В коде используйте цикл for, строковые методы upper() (преобразование к верхнему регистру) и lower() (преобразование к нижнему регистру),
# а также методы isupper() и islower(), проверяющие регистр строки или символа. Выполните срез строки с 1 по предпоследний символ.

from curses.ascii import islower, isupper

#способ в одну строчку
def inversionUpperLowerEasy(str):
    inverted_str = str.swapcase()
    return inverted_str

def inversionUpperLower(str):
    inverted_str = ""
    #инверсионная замена заглавных на прописные и наоборот
    for i in str:
        if islower(i):
            inverted_str += i.upper()
        elif isupper(i):
            inverted_str += i.lower()


    print(inverted_str[0:len(inverted_str )- 1])#срез с первого по предпоследний символ
    return inverted_str

str = input("Введите строку, включающую заглавные и прописные буквы: ")

print(inversionUpperLower(str))