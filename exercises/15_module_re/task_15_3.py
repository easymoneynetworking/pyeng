# -*- coding: utf-8 -*-
"""
Задание 15.3

Создать функцию convert_ios_nat_to_asa, которая конвертирует правила NAT из синтаксиса cisco IOS в cisco ASA.

Функция ожидает такие аргументы:
- имя файла, в котором находится правила NAT Cisco IOS
- имя файла, в который надо записать полученные правила NAT для ASA

Функция ничего не возвращает.

Проверить функцию на файле cisco_nat_config.txt.

Пример правил NAT cisco IOS
ip nat inside source static tcp 10.1.2.84 22 interface GigabitEthernet0/1 20022
ip nat inside source static tcp 10.1.9.5 22 interface GigabitEthernet0/1 20023

И соответствующие правила NAT для ASA:
object network LOCAL_10.1.2.84
 host 10.1.2.84
 nat (inside,outside) static interface service tcp 22 20022
object network LOCAL_10.1.9.5
 host 10.1.9.5
 nat (inside,outside) static interface service tcp 22 20023

В файле с правилами для ASA:
- не должно быть пустых строк между правилами
- перед строками "object network" не должны быть пробелы
- перед остальными строками должен быть один пробел

Во всех правилах для ASA интерфейсы будут одинаковыми (inside,outside).
"""
import re
from pprint import pprint
regex = r'ip nat inside source +(?P<method>\S+) +(?P<protocol>\S+) +(?P<address>[\d.]+) +(?P<port_in>\d+) +\w+ +[\w/]+ +(?P<port_out>\d+)'


def convert_ios_nat_to_asa(r_filename,w_filename):
    with open(r_filename) as src,open(w_filename,'w') as dest:
        for line in src:
            match = re.search(regex, line)
            if match:
                address1 = match.group('address')
                protocol1 = match.group('protocol')
                port_in1 = match.group('port_in')
                port_out1 = match.group('port_out')
                dest.write(f'object network LOCAL_{address1}\n'
                           f' host {address1}\n'
                           f' nat (inside,outside) static interface service {protocol1} {port_in1} {port_out1}\n')

convert_ios_nat_to_asa('cisco_nat_config.txt','test_asa.txt')
