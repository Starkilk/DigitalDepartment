list = [2, 3545, 3, 45, 123, 1, 34, 5, 65, 6, 2, 412, 34, 68, 967, 76, 533]

counter = 0

digit = int(input("Введите число: "))

for i in list:
    if i % digit == 0:
        counter += 1

print(counter)