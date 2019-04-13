# Задание на закрепление знаний по модулю json. Есть файл orders в формате JSON с информацией о заказах.
# Написать скрипт, автоматизирующий его заполнение данными. Для этого:
#
# Создать функцию write_order_to_json(), в которую передается 5 параметров — товар (item), количество
# (quantity), цена (price), покупатель (buyer), дата (date). Функция должна предусматривать запись
# данных в виде словаря в файл orders.json. При записи данных указать величину отступа в 4 пробельных символа;
#
# Проверить работу программы через вызов функции write_order_to_json() с передачей в нее значений каждого параметра.

import json


def write_order_to_json(item, quantity, price, buyer, date):
    dict_order = dict(
        item = item,
        quantity = quantity,
        price = price,
        buyer = buyer,
        date = date
    )
    print(dict_order)
    with open('orders.json', 'w') as file:
        json.dump(dict_order, file, sort_keys=True, indent=2)



write_order_to_json('item', 5, 120, 'buyer', '13.04.2019')