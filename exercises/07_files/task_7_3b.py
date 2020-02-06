# -*- coding: utf-8 -*-
"""
Задание 7.3b

Сделать копию скрипта задания 7.3a.

Дополнить скрипт:
- Запросить у пользователя ввод номера VLAN.
- Выводить информацию только по указанному VLAN.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

mac_table = []
ask = input('Enter Vlan number: ')

with open("CAM_table.txt", "r") as conf:
    for line in conf:
        line = line.split()
        if line and line[0].isdigit():
            if line[0] == ask:
                vlan, mac, _, intf = line
                print(f"{vlan:<9}{mac:20}{intf}")

# Все отлично

# вариант решения

user_vlan = input("Enter VLAN number: ")

with open("CAM_table.txt", "r") as conf:
    for line in conf:
        line = line.split()
        if line and line[0].isdigit() and line[0] == user_vlan:
            vlan, mac, _, intf = line
            print(f"{vlan:9}{mac:20}{intf}")
