# -*- coding: utf-8 -*-
"""
Задание 15.5

Создать функцию generate_description_from_cdp, которая ожидает как аргумент
имя файла, в котором находится вывод команды show cdp neighbors.

Функция должна обрабатывать вывод команды show cdp neighbors и генерировать на основании вывода команды описание для интерфейсов.

Например, если у R1 такой вывод команды:
R1>show cdp neighbors
Capability Codes: R - Router, T - Trans Bridge, B - Source Route Bridge
                  S - Switch, H - Host, I - IGMP, r - Repeater

Device ID        Local Intrfce     Holdtme    Capability  Platform  Port ID
SW1              Eth 0/0           140          S I      WS-C3750-  Eth 0/1

Для интерфейса Eth 0/0 надо сгенерировать такое описание
description Connected to SW1 port Eth 0/1

Функция должна возвращать словарь, в котором ключи - имена интерфейсов, а значения - команда задающая описание интерфейса:
'Eth 0/0': 'description Connected to SW1 port Eth 0/1'


Проверить работу функции на файле sh_cdp_n_sw1.txt.
"""
import re
from pprint import pprint


def generate_description_from_cdp(filename):
    regex = r'(?P<device>\S\d) +(?P<local_interface>\S+ [\d/]+) +\d+ +\w \w \w +\d+ +(?P<dest_interface>\S+ [\d/]+)'
    result = {}
    with open(filename) as f:
        for m in re.finditer(regex, f.read()):
            device = m.group('device')
            interface_local = m.group('local_interface')
            interface_dest = m.group('dest_interface')
            stri = f'description Connected to {device} port {interface_dest}'
            result[interface_local] = stri
    return result


generate_description_from_cdp('sh_cdp_n_sw1.txt')

# Все отлично

# вариант решения

def generate_description_from_cdp(sh_cdp_filename):
    regex = re.compile(
        r"(?P<r_dev>\w+)  +(?P<l_intf>\S+ \S+)"
        r"  +\d+  +[\w ]+  +\S+ +(?P<r_intf>\S+ \S+)"
    )
    description = "description Connected to {} port {}"
    intf_desc_map = {}
    with open(sh_cdp_filename) as f:
        for match in regex.finditer(f.read()):
            r_dev, l_intf, r_intf = match.group("r_dev", "l_intf", "r_intf")
            intf_desc_map[l_intf] = description.format(r_dev, r_intf)
    return intf_desc_map

