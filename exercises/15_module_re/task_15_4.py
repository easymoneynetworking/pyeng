# -*- coding: utf-8 -*-
"""
Задание 15.4

Создать функцию get_ints_without_description, которая ожидает как аргумент
имя файла, в котором находится конфигурация устройства.


Функция должна обрабатывать конфигурацию и возвращать список имен интерфейсов,
на которых нет описания (команды description).

Пример интерфейса с описанием:
interface Ethernet0/2
 description To P_r9 Ethernet0/2
 ip address 10.0.19.1 255.255.255.0
 mpls traffic-eng tunnels
 ip rsvp bandwidth

Интерфейс без описания:
interface Loopback0
 ip address 10.1.1.1 255.255.255.255

Проверить работу функции на примере файла config_r1.txt.
"""
import re
from pprint import pprint
regex = r'interface (\S+\d+)'

def get_ints_without_description(filename):
    all_interface = []
    desc_interface = []
    final_spisok = []
    with open(filename, 'r') as f:
        for line in f:
            m = re.search(regex,line)
            if m:
                a = m.group(1)
                all_interface.append(a)
            if line.startswith(' description'):
                desc_interface.append(a)
            final_spisok = [item for item in all_interface if item not in desc_interface]
    return final_spisok

print(get_ints_without_description('config_r1.txt'))



# Все отлично, только пропустил один интерфейс, чтобы он попал надо переделать регулярку
# interface Ethernet0/3.100
#  encapsulation dot1Q 100
#  xconnect 10.2.2.2 12100 encapsulation mpls
#   backup peer 10.4.4.4 14100
#   backup delay 1 1

# вариант решения

def get_ints_without_description2(config):
    regex = re.compile(r"!\ninterface (?P<intf>\S+)\n"
                       r"(?P<descr> description \S+)?")
    with open(config) as src:
        match = regex.finditer(src.read())
        result = [m.group('intf') for m in match if m.lastgroup == 'intf']
        return result

