#3.	Создайте кортеж, в котором храниться информация о результатах соревнований по волейболу. Поступают только те команды, у которых результат выше среднего. Поставьте программу, которая определяет победителей.
from collections import namedtuple

def teamsAboveAverage():
    n = int(input("Введите число команд: "))
    average = 0
    teams = tuple([int(input("Введите очки команды: ")) for _ in range(n)])

    for i in range(n):
        average +=teams[i]

    average //= n

    print(f"Среднее арифметическое {average}")
    for i in range(n):
        if teams[i] > average:
            print(f"Команда проша {teams[i]}")

    winer = teams[0]
    for i in range(n):
        if winer < teams[i]:
            winer = teams[i]

    print(f"Победитель {winer}")

teamsAboveAverage()






