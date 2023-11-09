#2.	В заданной строке символов найдите все «слова», написанные капсом (то есть строго заглавными), возможно внутри настоящих слов (аааБББввв).

string = input("Введите строку: ")
worsArr = string.split(" ")

wodsUpper = []

for i in worsArr:
    if i.isupper():
        wodsUpper.append(i)

print(wodsUpper)