import random
def createDictionary():
    length = int(input("Введите кол-во символов в строке: "))
    digitsKeys = [str(random.randint(0, 9)) for _ in range(length)]
    values =[0] * length

    print(digitsKeys)#для проверки

    #заполнение списка со значениями(Количество символов встретившихся в строке)
    for i in range(len(digitsKeys)):
        values[i] = digitsKeys.count(digitsKeys[i])

    print(values)#для проверки

    #формирование словаря из двух листов
    dictionary = dict(zip(digitsKeys, values))
    return dictionary



print(createDictionary())