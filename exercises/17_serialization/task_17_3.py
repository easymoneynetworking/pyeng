# -*- coding: utf-8 -*-
"""
Задание 17.3

Создать функцию parse_sh_cdp_neighbors, которая обрабатывает
вывод команды show cdp neighbors.

Функция ожидает, как аргумент, вывод команды одной строкой (не имя файла).
Функция должна возвращать словарь, который описывает соединения между устройствами.

Например, если как аргумент был передан такой вывод:
R4>show cdp neighbors

Device ID    Local Intrfce   Holdtme     Capability       Platform    Port ID
R5           Fa 0/1          122           R S I           2811       Fa 0/1
R6           Fa 0/2          143           R S I           2811       Fa 0/0

Функция должна вернуть такой словарь:
{'R4': {'Fa 0/1': {'R5': 'Fa 0/1'},
        'Fa 0/2': {'R6': 'Fa 0/0'}}}

Интерфейсы должны быть записаны с пробелом. То есть, так Fa 0/0, а не так Fa0/0.


Проверить работу функции на содержимом файла sh_cdp_n_sw1.txt
"""
import re
from pprint import pprint

regex = r'(?P<device_local>\w+\d+)>'
regex2 =  (r'(?P<device_dest>\w+\d+) +'
           r'(?P<local_interface>\w+ +\d[/]\d) +'
           r'\d+ +\w \w \w +\d+ +(?P<interface_dest>\w+ \d[/]\d)')

def parse_sh_cdp_neighbors(filenames):
    result_dic = {}
    result1 = re.search(regex, filenames)
    a = result1.group(1)
    result_dic[a] = {}
    for string in re.finditer(regex2, filenames):
        local_interface = string.group('local_interface')
        result_dic[a][local_interface] = {}
        device_dest = string.group('device_dest')
        interface_dest = string.group('interface_dest')
        result_dic[a][local_interface][device_dest] = interface_dest
    return result_dic



if __name__ == "__main__":
    with open('sh_cdp_n_sw1.txt', 'r') as f:
        pprint(parse_sh_cdp_neighbors(f.read()))
