# 5. Выполнить пинг веб-ресурсов yandex.ru, youtube.com и преобразовать результаты из байтовового
# в строковый тип на кириллице.

from subprocess import Popen, PIPE

args = ['ping', 'yandex.ru']

subproc_ping = Popen(args, stdout=PIPE)
for line in subproc_ping.stdout:
    line = line.decode('cp866').encode('utf-8')
    print(line.decode('utf-8'), end='')


args = ['ping', 'youtube.com']

subproc_ping = Popen(args, stdout=PIPE)
for line in subproc_ping.stdout:
    line = line.decode('cp866')
    print(line, end='')

with Popen(args=['ipconfig', '/all'], stdout=PIPE) as proc:
    for line in proc.stdout:
        line = line.decode('cp866')
        print(line, end='')
