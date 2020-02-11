# -*- coding: utf-8 -*-
"""
Задание 9.3a

Сделать копию функции get_int_vlan_map из задания 9.3.

Дополнить функцию:
    - добавить поддержку конфигурации, когда настройка access-порта выглядит так:
            interface FastEthernet0/20
                switchport mode access
                duplex auto
      То есть, порт находится в VLAN 1

В таком случае, в словарь портов должна добавляться информация, что порт в VLAN 1
      Пример словаря: {'FastEthernet0/12': 10,
                       'FastEthernet0/14': 11,
                       'FastEthernet0/20': 1 }

У функции должен быть один параметр config_filename, который ожидает как аргумент имя конфигурационного файла.

Проверить работу функции на примере файла config_sw2.txt


Ограничение: Все задания надо выполнять используя только пройденные темы.
"""


def get_int_vlan_map(config_filename):
    access_dic = {}
    access_dic1 = {}
    trunk_dic = {}
    vlan1 = 1
    with open(config_filename, 'r') as f:
        for line in f:
            if 'Fast' in line:
                acce_interface = line.split()[1]
            if 'access vlan' in line:
                access_dic[acce_interface] = int(line.split()[3])
            elif 'mode access' in line:
                    access_dic[acce_interface] = vlan1
            elif 'trunk allowed vlan' in line:
                trunk_dic[acce_interface] = [int(i) for i in line.split()[4].split(',')]
        return access_dic,trunk_dic

print(get_int_vlan_map('config_sw2.txt'))

