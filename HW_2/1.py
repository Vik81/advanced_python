# Задание на закрепление знаний по модулю CSV. Написать скрипт, осуществляющий выборку определенных данных из
# файлов info_1.txt, info_2.txt, info_3.txt и формирующий новый «отчетный» файл в формате CSV. Для этого:
#
# Создать функцию get_data(), в которой в цикле осуществляется перебор файлов с данными, их открытие и считывание
# данных. В этой функции из считанных данных необходимо с помощью регулярных выражений извлечь значения параметров
# «Изготовитель системы», «Название ОС», «Код продукта», «Тип системы». Значения каждого параметра поместить в
# соответствующий список. Должно получиться четыре списка — например, os_prod_list, os_name_list, os_code_list,
# os_type_list. В этой же функции создать главный список для хранения данных отчета — например, main_data — и
# поместить в него названия столбцов отчета в виде списка: «Изготовитель системы», «Название ОС», «Код продукта»,
# «Тип системы». Значения для этих столбцов также оформить в виде списка и поместить в файл main_data (также для
# каждого файла);

import csv
import re


def get_data():
    strings = ['Изготовитель системы', 'Название', 'Код продукта', 'Тип системы']    
    lst_file = ['info_1.txt', 'info_2.txt', 'info_3.txt']
    os_prod_list = []
    os_name_list = []
    os_code_list = []
    os_type_list = []

    for item in lst_file: 
        with open(item) as file:
            file_reader = csv.reader(file, delimiter=':')
            for row in file_reader:
                for string in strings:
                    match = re.search(string, str(row))
                    if match:
                        if string == strings[0]:
                            os_prod_list.append(str(row[1]).lstrip())
                        elif string == strings[1]:
                            os_name_list.append(str(row[1]).lstrip())
                        elif string == strings[2]:
                            os_code_list.append(str(row[1]).lstrip())
                        else:
                            os_type_list.append(str(row[1]).lstrip())

    with open('main_data', 'w') as file:
        file.write(str(strings))

    return os_prod_list, os_name_list, os_code_list, os_type_list


# Создать функцию write_to_csv(), в которую передавать ссылку на CSV-файл. В этой функции реализовать получение
# данных через вызов функции get_data(), а также сохранение подготовленных данных в соответствующий CSV-файл;
def write_to_csv(file_csv):
    with open(file_csv, 'w') as file:
        writer = csv.writer(file)
        for row in get_data():
            writer.writerow(row)


# Проверить работу программы через вызов функции write_to_csv().
write_to_csv('file.csv')