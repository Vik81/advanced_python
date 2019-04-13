# Задание на закрепление знаний по модулю yaml. Написать скрипт, автоматизирующий сохранение данных в файле
# YAML-формата. Для этого:
#
# Подготовить данные для записи в виде словаря, в котором первому ключу соответствует список, второму —
# целое число, третьему — вложенный словарь, где значение каждого ключа — это целое число с юникод-символом,
# отсутствующим в кодировке ASCII (например, €);
#
# Реализовать сохранение данных в файл формата YAML — например, в файл file.yaml. При этом обеспечить стилизацию
# файла с помощью параметра default_flow_style, а также установить возможность работы с юникодом: allow_unicode = True;
#
# Реализовать считывание данных из созданного файла и проверить, совпадают ли они с исходными'
# \\U00A9'
#
import yaml


dict_yaml = {
    'lst': ['1', '2', '3', '4'],
    'int': 10,
    'unicode_sym': {'copy': '#169', 'cent': '\\U00A2'} #пока не совсем понятно как вывести сам символ
}


with open('data.yaml', 'w') as file:
    yaml.dump(dict_yaml, file, default_flow_style=False, allow_unicode = True)

with open('data.yaml', 'r') as file:
    file_content = yaml.load(file)
    print(file_content)

print(dict_yaml)