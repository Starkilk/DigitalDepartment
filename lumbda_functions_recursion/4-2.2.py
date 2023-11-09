def fun(numbers):
    unique_numbers = set(numbers)
    return len(unique_numbers)


numbers = [1, 2, 3, 4, 5, 1, 2, 3, 4]
count = fun(numbers)
print("Количество различных чисел:", count)