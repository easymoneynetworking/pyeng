# -*- coding: utf-8 -*-
"""
Задание 22.1

Создать функцию parse_command_output. Параметры функции:
* template - имя файла, в котором находится шаблон TextFSM (templates/sh_ip_int_br.template)
* command_output - вывод соответствующей команды show (строка)

Функция должна возвращать список:
* первый элемент - это список с названиями столбцов
* остальные элементы это списки, в котором находятся результаты обработки вывода

Проверить работу функции на выводе команды output/sh_ip_int_br.txt и шаблоне templates/sh_ip_int_br.template.

"""
from pprint import pprint
import textfsm

def parse_command_output(template, command_output):
    finish_list = []
    with open(template) as f:
        re_table = textfsm.TextFSM(f)
        header = re_table.header
        finish_list.append(header)
        result = re_table.ParseText(command_output)
        for results in result:
            finish_list.append(results)
    return finish_list


if __name__ == '__main__':
    with open('output/sh_ip_int_br.txt') as output:
        outputs = output.read()
        pprint(parse_command_output('templates/sh_ip_int_br.template', outputs))


