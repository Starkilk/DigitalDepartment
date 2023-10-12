#4.5 ЗАДАНИЕ №3.
# Создайте простой тест, включающий 3 вопроса, на которые требуется ответить, да и нет. Создайте исключение неверного ввода ответа на вопрос.

try:
    answer1 = input("Вы сегодня завтракали? Да или Нет: ")
    if (answer1 != "Да") and (answer1 != "да") and (answer1 != "нет") and (answer1 != "Нет"):
        raise ValueError("Неправильный ввод")  # определили ошибку

    answer2 = input("А обедали? Да или Нет: ")
    if answer2 != "Да" and answer2 != "да" and answer2 != "нет" and answer2 != "Нет":
        raise ValueError("Неправильный ввод")  # определили ошибку

    answer3 = input("Может ужинали? Да или Нет: ")
    if answer3 != "Да" and answer3 != "да" and answer3 != "нет" and answer3 != "Нет":
        raise ValueError("Неправильный ввод")  # определили ошибку

    print("Ну и славно :)")
except ValueError as e:
    print(f"Ошибка: {e}")