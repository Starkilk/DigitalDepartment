import os


def check_file_existence(file_name):
    # Проверка существования файла
    if not os.path.isfile(file_name):
        # Создание файла
        with open(file_name, 'w') as f:
            files_list = os.listdir('.')
            files_list_str = '\n'.join(files_list)
            f.write(files_list_str)

    # Переименование файла
    renamed_file_name = 'new_file.txt'
    os.rename(file_name, renamed_file_name)

    # Вывод содержимого переименованного файла
    with open(renamed_file_name, 'r') as f:
        file_contents = f.read()
        print(file_contents)


check_file_existence("file.txt")