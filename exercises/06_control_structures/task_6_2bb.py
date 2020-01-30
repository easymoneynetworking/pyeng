# -*- coding: utf-8 -*-
"""
Задание 6.2a

Сделать копию скрипта задания 6.2.

Добавить проверку введенного IP-адреса. Адрес считается корректно заданным, если он:
   - состоит из 4 чисел разделенных точкой
   - каждое число в диапазоне от 0 до 255

Если адрес задан неправильно, выводить сообщение:
'Неправильный IP-адрес'

Сообщение должно выводиться только один раз.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

ip_address = input('Введите IP-адреса в формате x.x.x.x: ')

correct_ip = True
parts = ip_address.split(".")
normal_address = '10.0.1.1'

while correct_ip == True:
    for item in parts:
        if item.isdigit() == False:
            correct_ip = False
        elif 0 < int(item) > 255:
            correct_ip = False
        elif len(parts) != 4:
            correct_ip = False
        elif normal_address.count('.') != ip_address.count('.'):
            correct_ip = False
        elif correct_ip == False:
            print('Неправильный IP-адрес')
            ip_address = input('Введите IP-адреса в формате x.x.x.x: ')
        else:
            correct_ip = False

ip_list = ip_address.split(".")
oct1, oct2, oct3, oct4 = [
int(ip_list[0]),
int(ip_list[1]),
int(ip_list[2]),
int(ip_list[3]),
]
if oct1 in range(1, 223):
    print('unicast')
elif oct1 in range(224, 239):
    print('multicast')
elif ip_address == '255.255.255.255':
    print('local broadcast')
elif ip_address == '0.0.0.0':
    print('unassigned')
else:
    print('unused')

