#4.3 ЗАДАНИЕ №2.
# Выведите числа от 100 до 0, при выводе все четные числа заменяйте на знак %.

for i in range(100, -1,-1):
    if i % 2 == 0:
        print("%")
    else:
        print(i)