# -*- coding: utf-8 -*-
"""
Задание 17.3a

Создать функцию generate_topology_from_cdp, которая обрабатывает вывод команды show cdp neighbor из нескольких файлов и записывает итоговую топологию в один словарь.

Функция generate_topology_from_cdp должна быть создана с параметрами:
* list_of_files - список файлов из которых надо считать вывод команды sh cdp neighbor
* save_to_filename - имя файла в формате YAML, в который сохранится топология.
 * значение по умолчанию - None. По умолчанию, топология не сохраняется в файл
 * топология сохраняется только, если save_to_filename как аргумент указано имя файла

Функция должна возвращать словарь, который описывает соединения между устройствами, независимо от того сохраняется ли топология в файл.

Структура словаря должна быть такой:
{'R4': {'Fa 0/1': {'R5': 'Fa 0/1'},
        'Fa 0/2': {'R6': 'Fa 0/0'}},
 'R5': {'Fa 0/1': {'R4': 'Fa 0/1'}},
 'R6': {'Fa 0/0': {'R4': 'Fa 0/2'}}}

Интерфейсы должны быть записаны с пробелом. То есть, так Fa 0/0, а не так Fa0/0.

Проверить работу функции generate_topology_from_cdp на списке файлов:
* sh_cdp_n_sw1.txt
* sh_cdp_n_r1.txt
* sh_cdp_n_r2.txt
* sh_cdp_n_r3.txt
* sh_cdp_n_r4.txt
* sh_cdp_n_r5.txt
* sh_cdp_n_r6.txt

Проверить работу параметра save_to_filename и записать итоговый словарь в файл topology.yaml.

"""
import re
from pprint import pprint
import yaml
import glob

show_cdp_neighbor = glob.glob("sh_cdp_n_*.txt")
#pprint(show_cdp_neighbor)

def generate_topology_from_cdp(list_of_files,save_to_filename=None):
    result_dic = {}
    regex_attributes = (r'(?P<device>\S+) +(?P<local_interface>\w+ \d+/\d+) +'
                        r'\d+ +R? \S+ \S+ +\D+\d+\D +'
                        r'(?P<dest_interface>\w+ \d+/\d+)')
    regex_device = r'sh_cdp_n_(?P<device_local>\S+).txt'
    for  f in list_of_files:
        switch_match = re.search(regex_device, f)
        hostname = switch_match.group('device_local')
        hostname_upper_register = hostname.upper()
        result_dic[hostname_upper_register] = {}
        with open(f, 'r')as fi:
            for string in re.finditer(regex_attributes, fi.read()):
                local_interface = string.group('local_interface')
                result_dic[hostname_upper_register][local_interface] = {}
                device_dest = string.group('device')
                dest_interface = string.group('dest_interface')
                result_dic[hostname_upper_register][local_interface][device_dest] = dest_interface
    to_yaml = result_dic
    if save_to_filename:
        with open(save_to_filename, 'w') as fil:
            yaml.dump(to_yaml, fil)
    return result_dic



if __name__ == "__main__":
    pprint(generate_topology_from_cdp(show_cdp_neighbor,'cdp_neigbors.yml'))


