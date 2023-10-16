#Найти наибольшее количество идущих подряд пробелов

string = input("Введите текст: ")
maxSpace = 0
countSpace = 0

for i in string:
    if i == " ":
        countSpace += 1
    else:
        if countSpace > maxSpace:
            maxSpace = countSpace
            countSpace = 0
        else:
            countSpace = 0

if countSpace > maxSpace:
    maxSpace = countSpace

print(maxSpace)
