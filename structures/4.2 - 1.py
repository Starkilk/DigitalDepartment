#4.2 ЗАДАНИЕ №1.
# Найти max{min(a, b), min(c, d)}

a = int(input("Введите a: "))
b = int(input("Введите b: "))
c = int(input("Введите c: "))
d = int(input("Введите d: "))


var = {min(a, b), min(c, d)}
answer = max(var)
print(var)
print(answer)