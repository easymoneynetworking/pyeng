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

ip_address = input('Введите IP-адреса в формате 10.0.1.1: ')

correct_ip = True
parts = ip_address.split(".")
normal_address = '10.0.1.1'



for item in parts:
    if item.isdigit() == False:
        correct_ip = False
    elif 0 < int(item) > 255:
        correct_ip = False
    if len(parts) != 4:
        correct_ip = False
    elif normal_address.count('.') != ip_address.count('.'):
        correct_ip = False

if correct_ip == False:
   print('Неправильный IP-адрес')
else:
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


# Все отлично

# вариант решения

ip_address = input("Enter ip address: ")
octets = ip_address.split(".")
correct_ip = True

if len(octets) != 4:
    correct_ip = False
else:
    for octet in octets:
        # тут второе условие int(octet) in range(256)
        # проверяется только в том случае, если первое условие истина
        # Если встретился хоть один октет с нарушением,
        # дальше можно не смотреть
        if not (octet.isdigit() and int(octet) in range(256)):
            correct_ip = False
            break

if not correct_ip:
    print("Incorrect IPv4 address")
else:
    octets_num = [int(i) for i in octets]

    if octets_num[0] in range(1, 224):
        print("unicast")
    elif octets_num[0] in range(224, 240):
        print("multicast")
    elif set(octets_num) == {255}:
        print("broadcast")
    elif set(octets_num) == {0}:
        print("unassigned")
    else:
        print("unused")


####### Второй вариант

ip = input("Введите IP-адрес в формате x.x.x.x: ")
octets = ip.split(".")
valid_ip = len(octets) == 4

for i in octets:
    valid_ip = i.isdigit() and 0 <= int(i) <= 255 and valid_ip

if valid_ip:
    if 1 <= int(octets[0]) <= 223:
        print("unicast")
    elif 224 <= int(octets[0]) <= 239:
        print("multicast")
    elif ip == "255.255.255.255":
        print("local broadcast")
    elif ip == "0.0.0.0":
        print("unassigned")
    else:
        print("unused")
else:
    print("Неправильный IP-адрес")
