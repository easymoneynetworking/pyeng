# -*- coding: utf-8 -*-
"""
Задание 6.2

1. Запросить у пользователя ввод IP-адреса в формате 10.0.1.1
2. Определить тип IP-адреса.
3. В зависимости от типа адреса, вывести на стандартный поток вывода:
   'unicast' - если первый байт в диапазоне 1-223
   'multicast' - если первый байт в диапазоне 224-239
   'local broadcast' - если IP-адрес равен 255.255.255.255
   'unassigned' - если IP-адрес равен 0.0.0.0
   'unused' - во всех остальных случаях


Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

ip_address = input('Введите IP-адреса в формате 10.0.1.1: ')
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

ip_address = input("введите ip-адрес: ")
oct1 = int(ip_address.split(".")[0])

if ip_address == "255.255.255.255":
    print("local broadcast")
elif ip_address == "0.0.0.0":
    print("unassigned")
elif 1 <= oct1 <= 223:
    print("unicast")
elif 224 <= oct1 <= 239:
    print("multicast")
else:
    print("unused")

