# 4. Преобразовать слова «разработка», «администрирование», «protocol», «standard» из строкового представления в
# байтовое и выполнить обратное преобразование (используя методы encode и decode).

s1 = 'разработка'
s2 = 'администрирование'
s3 = 'protocol'
s4 = 'standard'

b_s1 = s1.encode('utf-8')
b_s2 = s2.encode('utf-8')
b_s3 = s3.encode('utf-8')
b_s4 = s4.encode('utf-8')

print(b_s1)
print(b_s2)
print(b_s3)
print(b_s4)

dec_s1 = b_s1.decode('utf-8')
dec_s2 = b_s2.decode('utf-8')
dec_s3 = b_s3.decode('utf-8')
dec_s4 = b_s4.decode('utf-8')

print(dec_s1)
print(dec_s2)
print(dec_s3)
print(dec_s4)
