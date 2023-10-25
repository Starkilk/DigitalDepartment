
#Используя форматированный вывод выведите изображение фигуры «Параллелограмма».
def draw_parallelogram(height, width):
    for i in range(height):
        # Распечатываем пробелы перед символами фигуры
        for j in range(height - i):
            print(" ", end="")
        # Распечатываем символы фигуры
        for k in range(width):
            print("*", end="")
        print()


draw_parallelogram(5, 10)