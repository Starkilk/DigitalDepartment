digit = int(input("Введите число: "))

while digit != 1 :
    digit /=2
    if digit < 1:
        break

if digit == 1:
    print("YES")
else:
    print("NO")