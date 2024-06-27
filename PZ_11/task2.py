# 2. Из предложенного текстового файла (text18-27.txt) вывести на экран его содержимое,
# количество пробельных символов. Сформировать новый файл, в который поместить текст
# в стихотворной форме предварительно поставив последнюю строку фразой введенной
# пользователем.


def task(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()

    # Вывод содержимого файла на экран
    print(f"Содержимое файла: {content}")

    # Подсчет количества пробельных символов
    whitespace_count = sum(1 for char in content if char.isspace())
    print(f"Количество пробельных символов: {whitespace_count}")

    # Получение пользовательской строки
    user_phrase = input("Введите фразу для добавления в конец файла: ")

    # Формирование нового файла с измененным текстом
    new_content = content + "\n" + user_phrase
    with open(f'modified_{filename}', 'w', encoding='utf-8') as file:
        file.write(new_content)


task('text18-27.txt')
