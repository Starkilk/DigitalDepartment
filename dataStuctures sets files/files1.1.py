size = 0
sredZnach = 0.0
list = []

#числа из файла поместили в список [[]]
with open("digits.txt")as file:
    for i in file:
        list.append([float(x) for x in i.split()])

#нашли среднее арифметическое значение
for i in list:
    sredZnach += i[0]
    size += 1
sredZnach /= size

print(list)
print(sredZnach)



