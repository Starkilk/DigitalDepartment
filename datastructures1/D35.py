s = input("Введите строку с пробелами: ")

tesrS = "aplikation and activity fire"

def sortWords(string):
    words = string.split()#преобразовали строку в список из подстрок
    words.sort(key=len)#отсортировали список по длинне элементов(слов)
    sortWord = " ".join(words)#прреобразуем отсортированный массив к строке str
    return sortWord

print(sortWords(s))
