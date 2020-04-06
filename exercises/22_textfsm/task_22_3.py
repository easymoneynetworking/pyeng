# -*- coding: utf-8 -*-
"""
Задание 22.3

Создать функцию parse_command_dynamic.

Параметры функции:
* command_output - вывод команды (строка)
* attributes_dict - словарь атрибутов, в котором находятся такие пары ключ-значение:
 * 'Command': команда
 * 'Vendor': вендор
* index_file - имя файла, где хранится соответствие между командами и шаблонами. Значение по умолчанию - "index"
* templ_path - каталог, где хранятся шаблоны. Значение по умолчанию - templates

Функция должна возвращать список словарей с результатами обработки вывода команды (как в задании 22.1a):
* ключи - имена переменных в шаблоне TextFSM
* значения - части вывода, которые соответствуют переменным

Проверить работу функции на примере вывода команды sh ip int br.
"""

from pprint import pprint
import textfsm
import clitable


def parse_command_dynamic(command_output, attributes_dict, index_file='index', templ_path='templates'):
    finish_dic = {}
    cli_table = clitable.CliTable(index_file, templ_path)
    cli_table.ParseCmd(command_output, attributes_dict)
    return [dict(zip(cli_table.header, item)) for item in cli_table]

if __name__ == "__main__":
    attributes_dict = {'Command': 'show ip int br' , 'Vendor': 'Cisco'}
    with open('output/sh_ip_int_br.txt') as output:
        outputs = output.read()
        pprint(parse_command_dynamic(outputs, attributes_dict))


# Все отлично

