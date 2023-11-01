#Из диапазона целых чисел m..n выделить:

# множество целых чисел, делящихся без остатка на K, или на L (K, L- простые)

# множество чисел делящихся на K*L без остатка

def fun(m, n):
    K = int(input("Введите число: "))
    L = int(input("Введите число: "))
    mn1 = set()
    mn2 = set()

    for i in range(m, n):
        if (i % K == 0) or (i % L == 0):
            mn1.add(i)

    for i in range(m, n):
        if (i % K == 0) and (i % L == 0):
            mn2.add(i)

    print(mn1)
    print(mn2)

fun(3,361)