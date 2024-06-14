import os
import shutil


def task1():
    '''Перейдите в каталог PZ_11. Выведите список всех файлов в этом каталоге.
    Имена вложенных подкаталогов выводить не нужно.'''
    os.chdir("../PZ_11")
    files_in_pz11 = [f for f in os.listdir() if os.path.isfile(f)]
    print("Список файлов в каталоге PZ_11:", files_in_pz11)


def task2():
    '''перейти в корень проекта, создать папку с именем test. В ней создать еще одну папку
    test1. В папку test переместить два файла из ПЗ 6, а в папку test1 - один файл из ПЗ 7.
    Файл из ПЗ7 переименовать в PZ_7.1.py. Вывести в консоль информацию о размере
    файлов в папке test.'''
    os.chdir('../')
    os.makedirs('test/test1', exist_ok=True)

    file_from_pz6 = 'PZ_6/PZ_6_27.py'
    file_from_pz7 = 'PZ_7/PZ_7_27.py'

    shutil.move(file_from_pz6, 'test/')
    shutil.move(file_from_pz7, 'test/test1/test.txt')

    files_in_test = [f for f in os.listdir('test') if os.path.isfile(os.path.join('test', f))]
    for file in files_in_test:
        file_size = os.path.getsize(os.path.join('test', file))
        print(f"Размер файла {file} в папке test: {file_size} байт")


def task4():
    '''Найти файл с самым коротким именем в папке PZ_11'''
    os.chdir('../PZ_11')
    shortest_name_file = min((f for f in os.listdir() if os.path.isfile(f)), key=len)
    print("Файл с самым коротким именем:", os.path.basename(shortest_name_file))


def task5():
    '''перейти в любую папку где есть отчет в формате .pdf и «запустите» файл в
    # привязанной к нему программе. Использовать функцию os.startfile().'''
    os.startfile('../reports/PZ_5.pdf')

    '''удалить файл test.txt.'''
    os.remove('../reports/PZ_2.pdf')
    print("Файл test.txt удален")