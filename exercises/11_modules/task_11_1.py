# -*- coding: utf-8 -*-
'''
Задание 11.1

Создать функцию parse_cdp_neighbors, которая обрабатывает
вывод команды show cdp neighbors.

У функции должен быть один параметр command_output, который ожидает как аргумент вывод команды одной строкой (не имя файла). Для этого надо считать все содержимое файла в строку,
а затем передать строку как аргумент функции.

Функция должна возвращать словарь, который описывает соединения между устройствами.

Например, если как аргумент был передан такой вывод:
"""
R4>show cdp neighbors

Device ID    Local Intrfce   Holdtme     Capability       Platform    Port ID
R5           Fa 0/1          122           R S I           2811       Fa 0/1
R6           Fa 0/2          143           R S I           2811       Fa 0/0
"""

Функция должна вернуть такой словарь:

    {('R4', 'Fa0/1'): ('R5', 'Fa0/1'),
     ('R4', 'Fa0/2'): ('R6', 'Fa0/0')}

В словаре интерфейсы должны быть записаны без пробела между типом и именем. То есть так Fa0/0, а не так Fa 0/0.

Проверить работу функции на содержимом файла sh_cdp_n_sw1.txt

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

from pprint import pprint

def parse_cdp_neighbors(command_output):
    test = command_output.split('\n')
    dictionary = {}
    for cdp in test:
        if '>' in cdp:
            r4 =  cdp.split('>')[0]
        elif cdp.startswith('R'):
            name, l_intf, l_n_intf, *other, r_intf = cdp.split()
            local_interface = l_intf + l_n_intf
            dest_interface = l_intf + r_intf
            dictionary[(r4,local_interface)] = (name,dest_interface)
    return dictionary

with open('sh_cdp_n_sw1.txt','r') as f:
    a = f.read()
    pprint(parse_cdp_neighbors(a))

# Все отлично

# вариант решения


def parse_cdp_neighbors(command_output):
    result = {}
    for line in command_output.split("\n"):
        line = line.strip()
        if ">" in line:
            hostname = line.split(">")[0]
        # отобрать нужные строки можно по последнему столбцу
        # последний символ число - номер интерфейса
        elif line and line[-1].isdigit():
            r_host, l_int, l_int_num, *other, r_int, r_int_num = line.split()
            result[(hostname, l_int + l_int_num)] = (r_host, r_int + r_int_num)
    return result


if __name__ == "__main__":
    with open("sh_cdp_n_sw1.txt", "r") as show_in:
        print(parse_cdp_neighbors(show_in.read()))
