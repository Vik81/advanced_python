# 6. Создать текстовый файл test_file.txt, заполнить его тремя строками: «сетевое программирование», «сокет»,
# «декоратор». Проверить кодировку файла по умолчанию. Принудительно открыть файл в формате Unicode и вывести
# его содержимое.

file = open('test_file.txt', 'w')
file.write('сетевое программирование\nсокет\nдекоратор')
file.close()

print(file)

with open('test_file.txt', 'r', encoding='utf-8') as file:
    for line in file:
        print(line, end='')

# но что-то пошло не так
