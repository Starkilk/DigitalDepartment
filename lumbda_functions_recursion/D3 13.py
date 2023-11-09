import re
import string
string1 = input("Введите строку: ")

def fun1(string):

    wordsArr = string.split(" ")
    wordsBb = []
    for word in wordsArr:
        if word[0] == 'b' or word[0] == 'B':
            wordsBb.append(word)

    print(wordsBb)

#fun1(string1)

##################################################
# def fun2(email):
#     pattern = r'^([\w\.-]+)@([\w\.-]+)\.([a-zA-Z\.-]+)$'
#     match = re.match(pattern, email)
#     if match:
#         login = match.group(1)
#         domain = match.group(2)
#         suffix = match.group(3)
#         return login, domain, suffix
#     else:
#         return None
#
# # Пример использования
# email1 = 'example.user@gmail.com'
# email2 = 'john.doe@example.com'
#
# parts1 = fun2(email1)
# parts2 = fun2(email2)
#
# if parts1:
#     login1, domain1, suffix1 = parts1
#     print(f"Логин: {login1}, Домен: {domain1}, Суффикс: {suffix1}")
# else:
#     print("Неверный формат email адреса.")
#
# if parts2:
#     login2, domain2, suffix2 = parts2
#     print(f"Логин: {login2}, Домен: {domain2}, Суффикс: {suffix2}")
# else:
#     print("Неверный формат email адреса.")

###############################

    def split_string(string, delimiters):
        pattern = '|'.join(map(re.escape, delimiters))
        return re.split(pattern, string)


    # Пример использования
    string = "разделитель1заданнойстрокипо, нескольким разделителям; потенциальным разделителям"
    delimiters = [",", ";"]
    result = split_string(string, delimiters)
    print(result)


def remove_punctuation(input_string):
    # Создаем пустую строку, в которую будем добавлять символы без пунктуации
    no_punct = ""

    # Проходимся по каждому символу входной строки
    for char in input_string:
        # Если символ не является символом пунктуации, добавляем его в результирующую строку
        if char not in string.punctuation:
            no_punct += char

    return no_punct


# Пример использования
input_string = "Привет! Как дела?"
result = remove_punctuation(input_string)
print(result)  # Выведет: "Привет Как дела"


