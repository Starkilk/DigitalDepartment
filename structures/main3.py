#ДЗ3. Напишите программу, которая запрашивает у пользователя числа до тех пор,
# пока каждое следующее число меньше 10. В конце программа сообщает, сколько чисел было введено


number = 0
counter = 0
while number < 10:
    number = int(input("Введите число: "))
    counter += 1
print(f"С учётом последнего числа(которое БОЛЬШЕ 10): {counter}")

print(f"БЕЗ учёта последнего числа(которое БОЛЬШЕ 10): {counter-1}")