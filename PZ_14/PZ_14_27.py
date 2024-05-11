# Из исходного текстового файла (Dostoevsky.txt) выбрать блок информации за 1857
# год и поместить ее в новый текстовый файл.

import re


def search_paragraph(input_file, year):
    start_flag = False
    text = []

    with open(input_file, "r", encoding="utf-8") as file:
        lines = file.readlines()

    for line in lines:
        if re.search("18", line) and start_flag:
            break

        if re.search(year, line):
            start_flag = True

        if start_flag:
            text.append(line)

    with(open(f'{year}.txt', 'w', encoding="utf-8")) as file:
        file.writelines(text)


search_paragraph("Dostoevsky.txt", "1857")
