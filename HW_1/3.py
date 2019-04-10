# 3. Определить, какие из слов «attribute», «класс», «функция», «type» невозможно записать в байтовом типе.
# import chardet

s1 = b'attribute'
# s2 = b'класс'    SyntaxError: bytes can only contain ASCII literal characters.
# s3 = b'функция'      SyntaxError: bytes can only contain ASCII literal characters.
s4 = b'type'

# print(chardet.detect(s1))
print(s1, s4)