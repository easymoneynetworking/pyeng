# -*- coding: utf-8 -*-
"""
Задание 22.1a

Создать функцию parse_output_to_dict.

Параметры функции:
* template - имя файла, в котором находится шаблон TextFSM (templates/sh_ip_int_br.template)
* command_output - вывод соответствующей команды show (строка)

Функция должна возвращать список словарей:
* ключи - имена переменных в шаблоне TextFSM
* значения - части вывода, которые соответствуют переменным

Проверить работу функции на выводе команды output/sh_ip_int_br.txt и шаблоне templates/sh_ip_int_br.template.
"""
from pprint import pprint
import textfsm


def parse_output_to_dict(template, command_output):
    finish_dic = {}
    with open(template) as f:
        re_table = textfsm.TextFSM(f)
        header = re_table.header
        result = re_table.ParseText(command_output)
        return [dict(zip(header, i)) for i in result]







if __name__ == '__main__':
    with open('output/sh_ip_int_br.txt') as output:
        outputs = output.read()
        pprint(parse_output_to_dict('templates/sh_ip_int_br.template', outputs))
