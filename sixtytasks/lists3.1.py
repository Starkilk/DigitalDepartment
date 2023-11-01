def sortEvenNumbers(arr):
    even_numbers = [num for num in arr if num % 2 == 0]  # список с четными числами
    sorted_numbers = sorted(even_numbers)  # список отсортированных четных чисел
    result = []
    index = 0
    # идём по изначальному массиву. если элемент чётный то берём его из отсортированного четного списка, если идёт нечетный, то вставляем элемент из изначального массива(как порядок нечётных чисел не нарушится)
    for num in arr:
        if num % 2 == 0:
            result.append(sorted_numbers[index])
            index += 1
        else:
            result.append(num)
    return result


arr = [2, 4, 445, 1, 45, 67, 10, 6, 34, 12]
print(sortEvenNumbers(arr))
