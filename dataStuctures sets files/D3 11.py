import os

largest_file = None#файл с максимальным размером
largest_size = 0#максимальный размер

for file in os.listdir():#проходим по всем файлам в текущем каталоге
    if os.path.isfile(file):#проверка, яявляетсяя ли файл обычным файлом
        file_size = os.path.getsize(file)#получаем размер файла
        if file_size > largest_size:#обычный аоиск наибольшего значения
            largest_size = file_size
            largest_file = file

if largest_file:
    print(f"Наибольший файл: {largest_file}, размер: {largest_size} байт")
else:
    print("Нет файлов в текущем каталоге")